from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('<int:pk>/detail', views.detail, name='detail'),
    path("login/", views.login, name="login"),
    path('password/', views.change_password, name='change_password'),
    path('', views.index, name="index"),
]

