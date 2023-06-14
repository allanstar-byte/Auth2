from django import forms
from myapp.models import CustomUser

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')
