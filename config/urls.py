from django.conf.urls import url
from django.contrib import admin
from v1.views import api_token, major, course, video

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # API tokens
    url(r'^v1/api-tokens/(?P<token>[\S]+)/$', api_token.view_single_token),

    # Majors
    url(r'^v1/majors/$', major.MajorView.as_view()),

    # Courses
    url(r'^v1/courses/(?P<major_slug>[\S]+)/$', course.CourseView.as_view()),

    # Videos
    url(r'^v1/videos/$', video.VideoView.as_view()),
]
