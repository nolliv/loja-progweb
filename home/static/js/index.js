function limpa_string(S) {
    // Deixa so' os digitos no numero
    var Digitos = "0123456789";
    var temp = "";
    var digito = "";
    for (var j = 0; j < S.length; j++) {
        digito = S.charAt(j);
        if (Digitos.indexOf(digito) >= 0) {
            temp = temp + digito
        }
    } //for
    return temp
} 

function valida_CPF(s) {
    var i;
    s = limpa_string(s);
    var c = s.substr(0,9);
    var dv = s.substr(9,2);
    var d1 = 0;
    for (i = 0; i < 9; i++)
    {
        d1 += c.charAt(i)*(10-i);
    }
    if (d1 == 0) return false;
    d1 = 11 - (d1 % 11);
    if (d1 > 9) d1 = 0;
    if (dv.charAt(0) != d1)
    {
        return false;
    }
    d1 *= 2;
    for (i = 0; i < 9; i++)
    {
        d1 += c.charAt(i)*(11-i);
    }
    d1 = 11 - (d1 % 11);
    if (d1 > 9) d1 = 0;
    if (dv.charAt(1) != d1)
    {
        return false;
    }
    return true;
} 

function createCookie(name, value, days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        var expires = "; expires="+date.toGMTString();
    }
    else var expires = "";
    document.cookie = name+"="+value+expires+"; path=/";
}

function readCookie(name) {
    var nameEQ = name + "=";
    var cookieArray = document.cookie.split(";");
    for (var i=0; i<cookieArray.length; i++) {
        var c = cookieArray[i];
        while (c.charAt(0)==' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

function eraseCookie(name) { createCookie(name,"",-1) }

$(document).ready(function(){
    $(".produto > a").click(function(event){
        href = $(this).attr('href');
        prodId = href.substring('comprar?ids='.length, href.length);
        prodsCarrinho = readCookie('prodsCarrinho');
        if (!prodsCarrinho) Produtos = prodId;
        else {
        //ATENCAO: Produtos com P maiuscolo para diferencias da div id=produtos!
            listaIds = prodsCarrinho.split(',');
            if($.inArray(prodId, listaIds) == -1)Produtos = prodsCarrinho + ',' + prodId;
        }
        createCookie('prodsCarrinho', Produtos);
        window.location = 'comprar?ids=' + Produtos;
        event.preventDefault();
    });    
});
