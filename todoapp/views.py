from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.


@login_required
def list_task(request):
    queryset = Task.objects.filter(author=request.user).order_by('complete', 'due')
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
        return redirect('/')
    context = {
        'tasks': queryset,
        'form': form,
    }
    return render(request, 'list_task.html', context)


@login_required
def update_task(request, pk):
    queryset = Task.objects.get(id=pk)
    form = UpdateForm(instance=queryset)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'update_task.html', context)


@login_required
def delete_task(request, pk):
    queryset = Task.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/')

    context = {
        'item': queryset
    }
    return render(request, 'delete_task.html', context)
