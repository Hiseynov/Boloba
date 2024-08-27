#forms.py

from django import forms  
from django.contrib.auth.forms import (AuthenticationForm,
                                       UserCreationForm,
                                       UsernameField,
                                       PasswordChangeForm,
                                       PasswordResetForm,
                                       SetPasswordForm)
from .models import User

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter Passowrd'}))
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter Password'}))
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email']
        
        widgets = { 
            'first_name' : forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Your first name'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Your last name'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control', 
                                              'placeholder': 'Your date'}),
            } 
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Şifreler eşleşmiyor")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Email Address'
        }))
        
class CustomSetPasswordForm(SetPasswordForm):
        new_password1 = forms.CharField(required=True, label='New Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your New Password'
                }))
        new_password2 = forms.CharField(required=True, label='Confirm New Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirm Your New Password'
                    }))
