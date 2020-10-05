from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/newpage", views.newpage, name="newpage"),
    path("wiki/<str:title>/", views.entry, name="entry")
]
