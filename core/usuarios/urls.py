from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
