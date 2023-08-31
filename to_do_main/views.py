from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        description = request.POST.get('description')

        Task.objects.create(
            title=title,
            description=description
        )

        return redirect('/')

    tasks = Task.objects.all()

    return render(request, 'list.html', {'tasks': tasks})


def update_task(request, id):
    changed_task = Task.objects.get(id=id)
    if request.method == 'POST':
        new_title = request.POST.get('new_title')
        new_description = request.POST.get('new_description')
        completed_checkbox = request.POST.get('completed')
        print('HERE', completed_checkbox)
        changed_task.title = new_title
        changed_task.description = new_description
        # changed_task.save()

        if completed_checkbox:
            changed_task.complete = True
        else:
            changed_task.complete = False
        changed_task.save()

        # changed_task.complete=True
        # if request.POST.get('completed'):
        #     changed_task.save()
        return redirect('/')
    return render(request, 'update.html', {'changed_task': changed_task})


def delete_task(request, id):
    # if request.method == 'POST':
    deleted_task = Task.objects.get(id=id)
    deleted_task.delete()
    return redirect('/')
