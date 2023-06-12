from django.urls import path
from . import views
app_name = 'static_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name= 'logout'),

]