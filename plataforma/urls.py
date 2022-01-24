from django.urls import path

from plataforma.views import home, imovel, agendar, agendamentos, cancelar_agendamento

app_name = 'plataforma'

urlpatterns = [
    path('', home, name='home'),
    path('imovel/<str:id>', imovel, name='imovel'),
    path('agendar/', agendar, name='agendar'),
    path('agendamentos/', agendamentos, name='agendamentos'),
    path('cancelar_agendamento/<str:id>', cancelar_agendamento, name="cancelar_agendamento")
]
