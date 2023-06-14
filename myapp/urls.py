from django.urls import path
from myapp.views import register_user

app_name = 'myapp'
urlpatterns = [
    path('', register_user, name='register'),
]
