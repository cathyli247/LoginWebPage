from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    
    class meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
       user = super(CreateUserForm, self).__init__(*args, **kwargs)
       self.fields['username'].required = False
    
#     def set_email(self, email):
#         user = super(CreateUserForm, self)
#         user.email = email
    
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.username = self.data['email']
  
        if commit:
            user.save()
