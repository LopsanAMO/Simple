from django.contrib import admin
from django.urls import path
from pages.views import home_bancomer, login_bancomer, escoti_click

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bancomer/', home_bancomer),
    path('bancomer/login', login_bancomer),
    path('escoti/click', escoti_click)
    # path('escoti/', home_escoti),
    # path('escoti/login', login_escoti)
]
