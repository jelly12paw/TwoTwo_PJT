from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('update/', views.update, name='update'),
    path('<int:pk>/detail', views.detail, name='detail'),
    path("login/", views.login, name="login"),
    path('create/', views.create, name='create'),
    path('password/', views.change_password, name='change_password'),
    path('delete/<int:pk>', views.delete, name="delete"),
]