
from django.contrib import admin
from django.urls import path, include
from event.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event/', include("event.urls"))
]
