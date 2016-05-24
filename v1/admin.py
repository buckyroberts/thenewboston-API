from django.contrib import admin
from .models import ApiToken, Subject, Playlist, Video


admin.site.register(ApiToken)
admin.site.register(Subject)
admin.site.register(Playlist)
admin.site.register(Video)
