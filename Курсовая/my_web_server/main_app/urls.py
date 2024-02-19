
from django.urls import path
from . import views
urlpatterns = [
    path('main', views.index, name='main page'),
    path('', views.about_us, name='about_us page'),
    path('create', views.create, name='create')
]