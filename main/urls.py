from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("contact/", views.contact, name="contact"),
] 