from django.shortcuts import render, redirect
from .models import Exercise, Muscle
from .forms import ExerciseForm, MuscleForm

def index(request):
    if request.method == 'POST':
        if 'add_muscle' in request.POST:
            muscle_form = MuscleForm(request.POST)
            if muscle_form.is_valid():
                muscle_form.save()
                return redirect('index')
        elif 'add_exercise' in request.POST:
            exercise_form = ExerciseForm(request.POST)
            if exercise_form.is_valid():
                exercise_form.save()
                return redirect('index')
    else:
        muscle_form = MuscleForm()
        exercise_form = ExerciseForm()

    muscles = Muscle.objects.all()
    exercises = Exercise.objects.all()

    return render(request, 'exercises/index.html', {
        'muscle_form': muscle_form,
        'exercise_form': exercise_form,
        'muscles': muscles,
        'exercises': exercises
    })

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
