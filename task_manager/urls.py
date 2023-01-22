from django.urls import path, include

from task_manager.views import index, by_category, TaskCreateView, delete, edit, complete

urlpatterns = [
    #path('', bonzay),
    path('<int:category_id>/', by_category, name='by_category_name'),
    path('', index, name='index'),
    path('add/', TaskCreateView.as_view(), name='add'),
    path('delete/<int:task_id>/', delete, name='delete_task'),
    path('edit/<int:task_id>/', edit, name='edit_task'),
    path('complete/<int:task_id>/', complete, name='complete_task'),


]