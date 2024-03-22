
from django.contrib import admin
from django.urls import include, path

from htmlproj.polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("export_card", views.export_card, name="export_card"),
]

