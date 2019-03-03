from django.contrib import admin
from .models import Asset,Task,Admin,Worker,TaskAssignment

# Register your models here.
admin.site.register(Asset)
admin.site.register(Task)
admin.site.register(Admin)
admin.site.register(Worker)
admin.site.register(TaskAssignment)
