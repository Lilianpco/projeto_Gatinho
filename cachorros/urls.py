from django.urls import path
from cachorros.views import * 

urlpatterns = [
    path('cadastro/', cadastro),
]
