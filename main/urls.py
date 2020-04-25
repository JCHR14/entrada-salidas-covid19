from django.conf.urls import url
from . import views
from django.conf import settings
from django.urls import path

urlpatterns = [
	path('', views.redirectLogin, name='redirectLogin'),
	path('entradas/', views.entradas, name='entradas'),
	path('salidas/', views.salidas, name='salidas'),
	#path('', views.redirectLogin, name='redirectLogin'),
	#path('activate/<str:uid>/<str:token>/', views.activate, name='activate'),
]
