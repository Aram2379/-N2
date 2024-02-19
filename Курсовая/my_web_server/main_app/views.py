from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Tasks
from .forms import TaskForm


def index(request: HttpRequest):
    tasks = Tasks.objects.order_by('-id')
    return render(request,'main_app/index.html', {'title':'Главная страница сайта', 'tasks':tasks})

def about_us(request):
    return render(request, 'main_app/about_us.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main page")

        else:
            error = "Задача была записана не коректно"

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    form = TaskForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'main_app/create.html', context)
