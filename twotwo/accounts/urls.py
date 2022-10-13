from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('password/', views.change_password, name='change_password'),
]