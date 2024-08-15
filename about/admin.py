from django.contrib import admin
from .models import  Education, Job, Skill


class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register([Education, Job, Skill], AboutAdmin)

