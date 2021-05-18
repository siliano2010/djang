from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    
   path('',views.index,name="index"),
   path('login',views.login,name="login"),
   path('cadastro',views.cadastro,name="cadastro"),
   url(r'criar/',views.criar,name="criar"),
   url(r'^entrar/',views.entrar,name="entrar"),
]
