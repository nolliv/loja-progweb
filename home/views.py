from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from home.models import Produto


def home(request):
    produtos = Produto.objects.all()
    return render_to_response('index.html',
                              {'produtos': produtos},
                              context_instance=RequestContext(request))

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
def comprar(request):
    query = request.GET['ids']
    lista_ids = query.split(',')
    #insira aqui uma list comprehension boladona que retorna os produtos!
    produtos = [ Produto.objects.get(id=prod_id) for prod_id in lista_ids ]

    return render_to_response('comprar.html',
                              {'produtos': produtos},
                             context_instance=RequestContext(request))
