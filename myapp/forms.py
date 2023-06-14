from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from myapp.models import CustomUser

class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = CustomUser
