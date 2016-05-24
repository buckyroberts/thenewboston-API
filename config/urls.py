from django.conf.urls import url
from django.contrib import admin
from v1.views import api_token, subject, playlist

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # API tokens
    url(r'^v1/api-tokens/(?P<token>[\S]+)/$', api_token.view_single_token),

    # Subjects
    url(r'^v1/subjects/$', subject.SubjectView.as_view()),

    # Playlists
    url(r'^v1/playlists/$', playlist.PlaylistView.as_view()),
]
