from django.contrib import admin
from django.urls import path
from pages.views import home_bancomer, login_bancomer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bancomer/', home_bancomer),
    path('bancomer/login', login_bancomer),
    # path('escoti/', home_escoti),
    # path('escoti/login', login_escoti)
]
