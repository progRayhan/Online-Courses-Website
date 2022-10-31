from django.contrib import admin
from courses.models import Course, Tag, Prerequisite, Learning

# Register your models here.
admin.site.register(Course)
admin.site.register(Tag)
admin.site.register(Prerequisite)
admin.site.register(Learning)