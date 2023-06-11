from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete<int:tskid>/', views.delete, name='delete'),
    path('update/<int:tskid>/', views.update, name='update'),
]
