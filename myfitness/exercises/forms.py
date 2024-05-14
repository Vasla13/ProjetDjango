# exercises/forms.py

from django import forms
from .models import Exercise, Muscle

class MuscleForm(forms.ModelForm):
    class Meta:
        model = Muscle
        fields = ['name']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'muscles_worked']

# exercises/views.py

from django.shortcuts import render, redirect
from .models import Exercise, Muscle
from .forms import ExerciseForm, MuscleForm

def add_muscle(request):
    if request.method == 'POST':
        form = MuscleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('muscle_list')
    else:
        form = MuscleForm()
    return render(request, 'exercises/add_muscle.html', {'form': form})

def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm()
    return render(request, 'exercises/add_exercise.html', {'form': form})

def muscle_list(request):
    muscles = Muscle.objects.all()
    return render(request, 'exercises/muscle_list.html', {'muscles': muscles})

def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercises/exercise_list.html', {'exercises': exercises})
