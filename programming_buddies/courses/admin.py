from django.contrib import admin
from courses.models import Course, Tag, Prerequisite, Learning

# Register your models here.
class TagAdmin(admin.TabularInline):
    model = Tag

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class LearningAdmin(admin.TabularInline):
    model = Learning

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, PrerequisiteAdmin, LearningAdmin]

admin.site.register(Course, CourseAdmin)