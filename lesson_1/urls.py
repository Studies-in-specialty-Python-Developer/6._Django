from django.urls import path
from . import views

app_name = 'lesson_1'

urlpatterns = [
    path('', views.index, name='index'),
    path('task_4/', views.task_4, name='task_4'),
]
