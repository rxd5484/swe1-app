from django.contrib import admin
from django.urls import include, path

from polls.views import index as polls_index

urlpatterns = [
    path("", polls_index, name="home"),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
