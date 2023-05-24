from django.contrib import admin

from students.models import student

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display = ("stdName", "stdID", "stdSex", "stdBirth")
    list_filter = ("stdName", "stdSex")
    list_field = ("stdName", "stdID")
    ordering = ("id",)

admin.site.register(student, studentAdmin)