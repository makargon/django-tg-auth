from django.contrib import admin
from django.urls import path, include
from auth_telegram.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]