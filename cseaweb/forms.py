from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class contactForms(forms.Form):
    name = forms.CharField(label='Name:',required = True ,max_length=100,help_text = 'max 100 chars allowed')
    email = forms.EmailField(required = True,label='E-mail:')
    comment = forms.CharField(label='Feedback:',required = True,widget=forms.Textarea)
    
