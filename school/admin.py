from django.contrib import admin
from school.models import Teacher, Activity, Schedule, Zanyatie, Enrollment


admin.site.register(Teacher)
admin.site.register(Activity)
admin.site.register(Schedule)
admin.site.register(Zanyatie)
admin.site.register(Enrollment)