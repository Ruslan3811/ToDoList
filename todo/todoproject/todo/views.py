from django.shortcuts import render, HttpResponseRedirect
from .models import ToDoList


# Create your views here.
def todoappView(request):
    all_to_do_items = ToDoList.objects.all()
    return render(request, 'todolist.html', {'all_items': all_to_do_items})

def addToDoView(request):
    x = request.POST['content']
    print("GET: ", x)
    new_item = ToDoList(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def delToDoView(request, i):
    obj = ToDoList.objects.get(id = i)
    obj.delete()
    return HttpResponseRedirect('/todoapp/')
