from django.urls import path
from django.urls import path
from .views import *


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', register, name="register"),
    path('success', success, name="success")
]