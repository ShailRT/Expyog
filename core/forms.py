from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import Profile
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ["username", "email", "user_type", "password1", "password2"]
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class EditProfile(forms.ModelForm):
        
    bio = forms.CharField()
    mobile = forms.CharField()
    email = forms.CharField()
    website = forms.CharField()
    country = forms.CharField()
    speciality = forms.CharField()
    
    class Meta:
        model = Profile
        fields = ['bio','mobile','email','website','country','speciality']

    def __init__(self, *args, **kwargs):
        super(EditProfile, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.required = False
    
    
    

    
