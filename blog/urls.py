from django.contrib import admin
from django.urls import path, include

from blog.views import *

urlpatterns = [
    path('', root_page, name='root_page'),

]
