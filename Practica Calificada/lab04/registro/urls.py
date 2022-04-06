from unicodedata import name
from django.urls import path

from . import views

app_name = 'registro'

urlpatterns = [
    # ex: /registro/
    path('', views.index, name='index'),
    # ex: /registro/5/
    path('<int:region_id>/', views.detalle, name='detalle'),
    # ex: /registro/candidato/5/
    path('candidato/<int:candidato_id>/', views.candidato, name='candidato'),
]
