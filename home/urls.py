from django.urls import path, include

from . import views
from galeria import urls as galeria_urls
from fale_conosco import urls as fale_conosco_urls

urlpatterns = [
    path('', views.home, name='home'),
    path('galeria', include(galeria_urls)),
    path('fale_conosco', include(fale_conosco_urls))
]