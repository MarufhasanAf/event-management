from django.urls import path
from event.views import test

urlpatterns = [
    path('test/', test)
]
