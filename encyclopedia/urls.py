from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get", views.get, name = "get"),
    path("newfile", views.newfile, name = "newfile"),
    path("errorpageexists", views.newfile, name = "errorpageexists"),
    path("editfile", views.editfile, name = "editfile"),
    path("editfile", views.get, name = "editfile"),
    path("randompage", views.randompage, name = "randompage"),
    path("randompage/<str:title>", views.randomget, name = "randomget")
]
    