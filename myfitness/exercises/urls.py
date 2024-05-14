from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_muscle/', views.add_muscle, name='add_muscle'),
    path('add_exercise/', views.add_exercise, name='add_exercise'),
    path('muscles/', views.muscle_list, name='muscle_list'),
    path('exercises/', views.exercise_list, name='exercise_list'),
]


