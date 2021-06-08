from django.urls import path 
from . import views 

urlpatterns =[
    path('',views.home,name='home'),
    path('todoapp/',views.todoapp,name='todoapp'),
    path('todoapp/delete/<int:todo_id>',views.delete_item,name='delete_item'),
    
]