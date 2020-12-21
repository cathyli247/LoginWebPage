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
    
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
  
        if commit:
            user.save()
            
     
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(username=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email address is already in use.')
      