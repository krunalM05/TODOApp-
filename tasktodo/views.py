from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import*
# Create your views here.
def home(request):
    tasks = task.objects.all()
    form = taskForm()
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {'tasks':tasks,'form':form}
    return render(request,'home.html',context)

def update(request, pk):
    uptask = task.objects.get(id=pk)
    form =taskForm(instance=uptask)
    if request.method == 'POST':
        form = taskForm(request.POST,instance=uptask)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'form':form}
    return render(request,'update.html',context)

def delete(request, pk):
    item = task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect("/")
    context = {'item':item}
    return render(request,'delete.html',context)