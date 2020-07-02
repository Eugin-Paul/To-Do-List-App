
from django.urls import path
from . import views

urlpatterns = [
        path('index', views.index, name = 'index'),
        path('add', views.addToDo, name = 'add'),
        path('completed/<todo_id>', views.completed, name = 'completed'),
        path('delete_completed', views.delete_completed, name = 'delete_completed'),
        path('delete_all', views.delete_all, name = 'delete_all')
]
