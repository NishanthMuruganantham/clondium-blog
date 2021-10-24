from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model, authenticate
from django.forms import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import Tab, TabHolder
from django.conf import settings

User = get_user_model()



class SignupForm(UserCreationForm):
    
    password1 = forms.CharField(label = "Password", widget = forms.PasswordInput(
        attrs = {'class': 'input100'}
    ))
    
    password2 = forms.CharField(label = "Confirm Password", widget = forms.PasswordInput(
        attrs = {'class': 'input100'}
    ))
    
    class Meta:
        model = User
        fields = ('email','username','password1','password2')
        
        widgets = {
            'username': forms.TextInput(
                attrs={'class':'input100'}
            ),
            'email': forms.EmailInput(
                attrs={'class':'input100'}
            ),
            'password1': forms.PasswordInput(
                attrs={'class':'input100'}
            ),
            'password2': forms.PasswordInput(
                attrs={'class':'input100'}
            )
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




class LoginForm(AuthenticationForm):
    
    
    username = forms.CharField(
        label = "username",
        widget = forms.EmailInput(
            
            attrs = {
                'class': 'input100'
            }
        )
    )
    
    password = forms.CharField(
        label = "password",
        widget = forms.PasswordInput(
            attrs = {
                'class': 'input100'
            }
        )
    )
    
    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = 'username or passoword is invalid'
        super().__init__(*args, **kwargs)


class ProfileEditForm(UserChangeForm):
    profile_picture = forms.ImageField(label=('profile_picture'),error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    
    class Meta:
        fields = (
            'username','first_name','last_name','email','profile_picture',
            'date_of_birth','bio','website',
            'facebook','instagram','linkedin','google_plus','twitter','github',
        )
        model = User
        
        widgets = {
            'username': forms.TextInput(
                attrs = {'class': 'form-control'}
            ),
            'first_name' : forms.TextInput(
                attrs = {'class': 'form-control'}
            ),
            'last_name' : forms.TextInput(
                attrs = {'class': 'form-control'}
            ),
            'email' : forms.TextInput(
                attrs = {'class': 'form-control'}
            ),
            'date_of_birth' : forms.DateInput(
                attrs = {'class': 'form-control','id':'datepicker'}
            ),
            'bio' : forms.Textarea(
                attrs = {'class': 'form-control'}
            ),
            'website' : forms.URLInput(
                attrs = {'class': 'form-control'}
            ),
            'facebook' : forms.URLInput(
                attrs = {'class': 'form-control'}
            ),
            'twitter' : forms.URLInput(
                attrs = {'class': 'form-control'}
            ),
            'instagram' : forms.URLInput(
                attrs = {'class': 'form-control'}
            ),
            'google_plus' : forms.URLInput(
                attrs = {'class': 'form-control'}
            ),
            'linkedin' : forms.URLInput(
                attrs = {'class': 'form-control'}
            ),
            'github' : forms.URLInput(
                attrs = {'class': 'form-control'}
            )
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].disabled = True
        self.fields['first_name'].required = False
        self.fields['bio'].widget.attrs['style']  = 'width:500px;height: 120px'


