from django.urls import path
from myapp.views import register_user
from myapp.views import login_view, landing_view
from myapp.views import register_user, login_view


app_name = 'myapp'
urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_view, name='login'),
    path('landing/', landing_view, name='landing'),
]



