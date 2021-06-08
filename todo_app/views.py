from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TodoApp
    # Create your views here.
def home(request):

    item = request.POST.get('add_item')
    if item:
        TodoApp.objects.create(items_added=item)
    return HttpResponseRedirect('/todoapp')


def todoapp(request):
    items = TodoApp.objects.all()
    context = {'items':items}
    return render(request,'todo_app/todoapp.html',context=context)

def delete_item(request,todo_id):
    id = todo_id
    item = TodoApp.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect('/todoapp')
    
    