from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import ToDoForm
from . import models
from django.urls import reverse_lazy

# Create your views here.
class CreateTaskView(FormView):
    template_name = 'home.html'
    form_class = ToDoForm
    success_url = reverse_lazy('task_list')  

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class TaskListView(ListView):
    model = models.ToDoModels
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class CompletedTaskListView(ListView):
    model = models.ToDoModels
    template_name = 'completed_task_list.html'
    context_object_name = 'tasks'


class EditTaskView(UpdateView):
    model = models.ToDoModels  
    form_class = ToDoForm 
    template_name = 'edit_task.html'  
    success_url = reverse_lazy('task_list') 

def complete_task(request, pk):
    task = get_object_or_404(models.ToDoModels, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('completed_task_list')

class DeleteTaskView(DeleteView):
    model = models.ToDoModels  
    template_name = 'delete_task.html'  
    success_url = reverse_lazy('task_list')  

