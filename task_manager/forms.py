from django.forms import ModelForm


from task_manager.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'descript', 'category')


















