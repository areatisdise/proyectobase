from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('forms/', views.forms, name='forms'),

]