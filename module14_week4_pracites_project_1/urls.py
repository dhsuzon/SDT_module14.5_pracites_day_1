
from django.contrib import admin
from django.urls import path,include
from . views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('',home_view),
]
