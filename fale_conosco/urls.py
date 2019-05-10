from django.urls import path

from . import views

urlpatterns = [
    path('', views.fale_conosco, name='fale_conosco')
]