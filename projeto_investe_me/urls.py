from django.contrib import admin
from django.urls import path
from investa_me import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.investimentos, name='investimentos'),
    path('novo_investimento/', views.criar, name='novo_investimento'),
    path('novo_investimento/<int:id_investimento>', views.editar, name='editar'),
    path('investimento_registrado/', views.investimento_registrado, name='investimento_registrado'),
    path('/<int:id_investimento>/', views.detalhe, name='detalhe'),
    path('excluir_investimento/<int:id_investimento>', views.excluir, name='excluir')
]
