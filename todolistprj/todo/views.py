from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView


from django.urls import reverse_lazy
from .models import Task


class TaskList(ListView):
    model = Task
    context_object_name = 'task'

class TaskDetail(DetailView):
    model = Task    
    context_object_name = 'task'
    template_name = 'todo/task_detail.html'


class TaskCreate(CreateView):
    model = Task 
    context_object_name = 'task'
    template_name = 'todo/task_from.html'
    fields = "__all__"
    #fields = ['title']
    success_url = reverse_lazy('task')

class TaskUpdate(UpdateView):
    model = Task    
    template_name = 'todo/task_from.html'
    fields = "__all__"
    success_url = reverse_lazy('task')