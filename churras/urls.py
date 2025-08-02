from django.urls import path
from .views import index, churrasco, buscar

urlpatterns = [
    path('', index, name='index'), # Página 
    path('buscar/', buscar, name='buscar'), # Página
    path('<int:id>', churrasco, name='churrasco'),
]