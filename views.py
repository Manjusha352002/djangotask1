from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def task_view(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', {'tasks': tasks})

