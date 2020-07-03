from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from file_system.models import File_System

admin.site.register(File_System, DraggableMPTTAdmin)
# Register your models here.
