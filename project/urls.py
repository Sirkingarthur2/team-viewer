# urls.py
from django.contrib import admin
from django.urls import path
from app.views import team_view

urlpatterns = [
    path('', team_view, name='home'),
    path('<str:team_name>/', team_view, name='team_view'),
    path('admin/', admin.site.urls),
]
