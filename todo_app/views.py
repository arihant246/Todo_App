from multiprocessing import context
from django.urls import reverse
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from .models import ToDoItem

# Create your views here.

def index (request):
    done_items = ToDoItem.objects.filter(todo_status="DONE")
    not_done_items = ToDoItem.objects.filter(todo_status="NOT DONE") 
    context= {
        "done_items" : done_items,
        "not_done_items" : not_done_items
    }
    return render(request, 'todo_app/index.html',context)

def mark_all_complete (request):
    not_done_items = ToDoItem.objects.filter(todo_status="NOT DONE")
    not_done_items.update(todo_status="DONE")
    return HttpResponseRedirect(reverse('todo_app:index'))

def insert_todo (request):
    todo_text = request.POST["todo_text"]
    obj = ToDoItem(todo_text=todo_text)
    obj.save()
    return HttpResponseRedirect(reverse('todo_app:index'))

def mark_done (request,id):
    obj = ToDoItem.objects.get(id=id)
    obj.todo_status = "DONE" 
    obj.save()
    return HttpResponseRedirect(reverse('todo_app:index'))
    

def delete_todo (request,id):
    obj = ToDoItem.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect(reverse('todo_app:index')) 
    
