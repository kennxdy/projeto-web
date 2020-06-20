from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('matriz', views.download_matriz, name='download_matriz'),
]
