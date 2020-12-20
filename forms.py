from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    
    class meta:
        model = User
        fields = ['email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
       super(CreateUserForm, self).__init__(*args, **kwargs)
       del self.fields['username']