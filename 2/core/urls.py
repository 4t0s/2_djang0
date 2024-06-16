from django.contrib import admin
from django.urls import path
from app.views import home, auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('login/', auth, name = 'auth')
]
