from django.urls import path
from . import views


# path, views도 중요하지만. urlpatterns 라는 변수가 필수적이다아!!!
urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/', views.detail),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update),
    path('<int:pk>/delete/', views.delete),

]