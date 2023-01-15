from django.urls import path

from . import views

urlpatterns = [
    path('/net', views.net, name='net'),
    path('/upcoming', views.upcoming, name='coming'),
]