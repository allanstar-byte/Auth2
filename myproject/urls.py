from django.contrib import admin
from django.urls import path, include
from myapp.views import landing_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', include('myapp.urls')),
    path('login/', login_view, name='login'),
    path('landing/', landing_view, name='landing'),
]
