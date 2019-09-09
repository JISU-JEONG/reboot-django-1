from django.urls import path
from . import views


# path, views도 중요하지만. urlpatterns 라는 변수가 필수적이다아!!!
urlpatterns = [
    path('', views.index),

]