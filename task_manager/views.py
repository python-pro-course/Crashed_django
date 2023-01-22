
# Create your views here.
from django.template import loader
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy


from task_manager.forms import TaskForm
from task_manager.models import Task, Category

class TaskCreateView(CreateView):
    template_name = 'task_manager/create_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

def bonzay(request):
    return HttpResponse("<h1>Бoнзaй>")

def index(request):
    #template = loader.get_template('task_manager/index.html')
    tasks = Task.objects.all()
    categories = Category.objects.all()
    return render(request, 'task_manager/index.html', {'tasks': tasks, 'categories' : categories})


def by_category(request, category_id):
    tasks = Task.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'tasks': tasks, 'categories': categories, 'current_category': current_category}
    return render(request, 'task_manager/by_category.html', context)

def delete(request, task_id):
    Task.objects.get(id=task_id).delete()
    return HttpResponseRedirect('/task_manager')

def edit(request, task_id):
    task_to_edit = Task.objects.get(id=task_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        task_to_edit.title = request.POST.get('title')
        task_to_edit.descript = request.POST.get('descript')
        category =  request.POST.get('category')
        task_to_edit.category = Category.objects.get(name=category)
        task_to_edit.save()
        return HttpResponseRedirect('/task_manager')
    else:
        return render(request, 'task_manager/edit.html', {'task': task_to_edit, 'categories': categories})
def complete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.status == False:
        task.status = True
        task.save()
    if task.status == True:
        task.status = False
        task.save()
    return render(request, 'task_manager/', {'status': task.status, 'task' : task})










