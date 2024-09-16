from django.contrib import admin
from .models import Faculty, Kafedra, Student, Subject, Teacher, Group


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'kafedra', 'group')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject')

@admin.register(Kafedra)
class KafedraAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'kafedra')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty')