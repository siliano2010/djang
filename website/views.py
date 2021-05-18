from django.shortcuts import render

from . import models






def index(resquest):
    return render(resquest,'index.php',{"radope":1})


def login(resquest):
    
    return render(resquest,'paginas/login.php',{"fail":''})

def entrar(resquest):
    email=resquest.POST.get('email')
    senha = resquest.POST.get('senha')

    x=models.authlogin(email,senha)
    if  x:
        return render(resquest,'paginas/painel.php',{"e":x})
    else:
        return render(resquest,'paginas/login.php',{"fail":'E-mail ou Senha Invalidos'})


def cadastro(resquest):
    return render(resquest,'paginas/cadastro.php',{})

def criar(resquest):
    email=str(resquest.POST.get('email').split("."))
    print(email)
    return render(resquest,'paginas/painel.php',{"e":email})