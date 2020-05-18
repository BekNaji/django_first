from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, get_list_or_404
from .models import Todo
# Create your views here.

def index(request):
    #todos = Todo.objects.all()
    todos = get_list_or_404(Todo)
    return render(request,"index.html",{"todos":todos})

def addTodo(request):
    if request.method == "GET":
        return redirect("/")
    else:
        title = request.POST.get("title")
        newTodo = Todo(title = title,comleted = False)

        newTodo.save()
        
        return redirect("/")

def edit(request,id):

    todo = get_object_or_404(Todo,id=id)
    return render(request,"edit.html",{"todo":todo})

def update(request):
     
    
    id = request.POST.get('id') 
    todo = get_object_or_404(Todo, id = id)

    todo.title = request.POST.get('title')
    todo.save()

    return redirect("/")

def delete(request,id):
    todo = get_object_or_404(Todo,id=id)

    todo.delete()
    return redirect("/")