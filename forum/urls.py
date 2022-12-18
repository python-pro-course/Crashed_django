from django.urls import path, include
from forum.views import *

urlpatterns = [
    path('', forum_1),
]