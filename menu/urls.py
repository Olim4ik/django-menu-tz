from django.urls import path
import menu.views as menu


urlpatterns = [
    path('', menu.index, name='index'),
    path('<str:pk>/', menu.index, name='index')
]   