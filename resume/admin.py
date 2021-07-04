from django.contrib import admin
from resume.models import *
# Register your models here.


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    search_fields = ['uuid', 'title', 'type']
    list_display = ['uuid', 'title', 'type']
