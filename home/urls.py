from django.urls import path
from . import views

urlpatterns = [
    # rota para view index
    
    path('', views.index, name='index'),
    
    path('sobre/', views.sobre, name='sobre'),
    
    path('contato/', views.contato, name='entre_em_contato'),
    
    path('item/<int:id>/', views.exibir_item, name='exibir_item'),
    
]