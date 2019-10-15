from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class feedbackform(forms.Form):
    cem = forms.CharField(label='College E-mail:',max_length=300)
    event_name = forms.CharField(label='Event Name:',max_length=100, required=True)
    fback = forms.CharField(label='Your Feedback:',max_length=600, required=True)
    
