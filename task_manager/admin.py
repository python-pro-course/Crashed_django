from django.contrib import admin

# Register your models here.
from .models import Task, Category

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'descript', 'when_created', 'category')
    list_display_links = ('title', 'descript', 'when_created')
    search_fields = ('title', 'descript')

admin.site.register(Task, TaskAdmin)
admin.site.register(Category)



