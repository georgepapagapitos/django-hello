from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("george", views.george, name="george"),
    path("ruby", views.ruby, name="ruby")
]