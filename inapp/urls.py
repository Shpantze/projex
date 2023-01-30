from django.urls import path

from . import views

app_name = 'inapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('addItem/', views.addItem, name='addItem')
]