from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from home.models import Produto


def home(request):
    produtos = Produto.objects.all()
    return render_to_response('index.html',
                              {'produtos': produtos},
                              context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username, password)
            user.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()

    return render_to_response('registrar.html', {'form': form},
                             context_instance=RequestContext(request))

@login_required
def carrinho(request):
    prod_id = request.GET['prod_id']
    #lista_ids = query.split(',')
    if not 'prod_ids' in request.session.keys():
        request.session['prod_ids'] = [prod_id]
    else:
        if prod_id not in request.session['prod_ids']:
            request.session['prod_ids'] += [prod_id]

    #insira aqui uma list comprehension boladona que retorna os produtos!
    produtos = [ Produto.objects.get(id=prod_id) for prod_id in request.session['prod_ids']]
    preco_total = 0
    for produto in produtos:
        sp = produto.preco.split(',')
        preco = 100 * int(sp[0]) + int(sp[1])
        preco_total += preco
    str_tot = unicode(preco_total)
    str_tot2 = str_tot[:-2] + ',' + str_tot[-2:]

    return render_to_response('carrinho.html',
                              {'produtos': produtos, 'tot': str_tot2},
                             context_instance=RequestContext(request))

@login_required
def finalizar_compra(request):
    for prod_id in request.session['prod_ids']:
        prod = Produto.objects.get(id=prod_id)
        prod.qtd_em_estoque -= 1
        prod.save()
    logout(request)
    return HttpResponseRedirect('/')
