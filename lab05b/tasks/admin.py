from django.contrib import admin
from .models import Tareas

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("creacion", )

admin.site.register(Tareas, TaskAdmin)

