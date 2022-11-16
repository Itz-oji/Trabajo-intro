from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .views import galeria, home, prueba, perropag, gatopag, mascota1pag, mascota2pag
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('index/', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('usuario/', prueba, name="subirperro"),
    # path('login/', login, name="vistalogin"),
    path('perro/', perropag, name="perropag" ),
    path('gato/', gatopag, name="gato" ),
    path('mascotas/', mascota1pag, name="mascota1pag" ),
    path('mascotass/', mascota2pag, name="mascota2pag" ),
    #path('login2/', auth_views.LoginView.as_view(template_name='app/registration/login2.html')),
    path('login/', LoginView.as_view(),name='login_url'),
    path('registro/', views.registerView,name='register_url'),
    path('logout/', LogoutView.as_view(),name='logout')
]
