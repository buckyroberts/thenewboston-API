from django.conf.urls import include, url
from django.contrib import admin
from v1.views import api_token, major, course, video

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # API
    url(r'^v1/api-tokens/(?P<token>[\S]+)/$', api_token.view_single_token),
    url(r'^v1/majors/$', major.MajorView.as_view(), name='majors'),
    url(r'^v1/videos/(?P<course_id>[\S]+)/$', video.VideoView.as_view(), name='videos'),
    url(r'^v1/videos/$', video.VideoView.as_view()),
    url(r'^v1/(?P<major_slug>[\S]+)/$', course.CourseView.as_view(), name='courses'),

    # Website
    url(r'^', include('website.urls')),
]
