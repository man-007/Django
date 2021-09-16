import re
from django.shortcuts import render, redirect
from django.contrib import messages
from mongoengine import connect
from pymongo import DESCENDING
from .forms import add_work
from .models import todo_lis
# Create your views here.
def home(request):
    connect(db="demo_db_2", host="localhost", port=27017)
    context = {}
    context['work'] = todo_lis.objects()
    if request.POST:
        form = add_work(request.POST)
        title = request.POST['task']
        print(title)
        Description = request.POST.get('description')
        print("Description =", Description)
        added_date = request.POST.get('date_added')
        print("added = ", added_date)
        form_2 = todo_lis(task=title, Description=Description, date_added=added_date)
        form_2.save()
        messages.success(request, f'{title} has been created!')
        return redirect('home')
    else:
        form = add_work()
    
    return render(request, 'home.html', {'data':context, 'form':form})

def delete(request, **kwargs):
    print(kwargs['pk'])
    if request.POST:
        id=kwargs['pk']
        todo_lis.objects(id=id).delete()
        messages.success(request, f'Task with id {id} has been deleted')
        return redirect('home')
    return render(request, 'delete.html', {})

def update(request, **kwargs):
    print(kwargs['pk'])
    id=kwargs['pk']
    connect(db="demo_db_2", host="localhost", port=27017)
    task = todo_lis.objects(id=id)
    if request.POST:
        form = add_work(request.POST)
        title = request.POST['task']
        print(title)
        Description = request.POST.get('description')
        print("Description =", Description)
        added_date = request.POST.get('date_added')
        print("added = ", added_date)
        todo_lis.objects(id=id).update(task=title, Description=Description, date_added=added_date)
        messages.success(request, f'Task with id {id} has been deleted')
        return redirect('home')
    else:
        form = add_work()
    return render(request, 'update.html', {'form':form})