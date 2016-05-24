from django.contrib import admin
from .models import ApiToken, Major, Course, Video


admin.site.register(ApiToken)
admin.site.register(Major)
admin.site.register(Course)
admin.site.register(Video)
