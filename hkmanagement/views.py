from django.shortcuts import render,get_object_or_404,redirect
from .models import Admin,Asset,Task,Worker,TaskAssignment
from datetime import datetime
from django.utils import timezone
from .forms import AssetForm,TaskAllocationForm,TaskForm,WorkerForm
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

import json

def display_assets(request):
    assets = Asset.objects.all()
    return render(request, 'hkmanagement/asset_list.html', {'assets': assets})

def get_tasks_for_worker(request,pk):
    ctx={
        'workerid':pk,
    }
    taskids = TaskAssignment.objects.filter(workerid=pk,timeOfAllocation__lte=datetime.now(),taskToBePerformedBy__gte=datetime.now()).values_list('taskid')
    tasks = Task.objects.filter(id__in=taskids)
    ctx.update({'tasks':tasks})
    taskscount = tasks.count()
    if taskscount>0: taskscount = 1
    ctx.update({'taskscount':taskscount})
    return render(request, 'hkmanagement/task_list.html', ctx)

@login_required
def add_asset(request):

    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'status':'Successfully added asset'}))
    else:
        form = AssetForm()
    return render(request,'hkmanagement/add_asset.html',{'form':form})

@login_required
def add_task(request):

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'status':"Successfully added task"}))
    else:
        form = TaskForm()
    return render(request,'hkmanagement/add_task.html',{'form':form})

@login_required
def add_worker(request):

    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'status':"Successfully added worker"}))
    else:
        form = WorkerForm()
    return render(request,'hkmanagement/add_worker.html',{'form':form})

@login_required
def allocate_task(request):
    
    if request.method == "POST":
        form = TaskAllocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'status':"Successfully allocated task"}))
    else:
        form = TaskAllocationForm()
    return render(request,'hkmanagement/allocate_task.html',{'form':form})
    