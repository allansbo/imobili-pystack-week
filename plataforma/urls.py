from django.urls import path

from plataforma.views import home, imovel

app_name = 'plataforma'

urlpatterns = [
    path('', home, name='home'),
    path('imovel/<str:id>', imovel, name="imovel"),
]
