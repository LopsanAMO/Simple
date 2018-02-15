from django.contrib import admin
from django.urls import path
from pages.views import home, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login', login)
]
