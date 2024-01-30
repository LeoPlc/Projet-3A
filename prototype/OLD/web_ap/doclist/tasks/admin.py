from django.contrib import admin
from tasks.models import Collection
from tasks.models import Task

# Register your models here.

admin.site.register(Task)
admin.site.register(Collection)