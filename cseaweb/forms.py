from django import forms
from .models import feedback
class contactForms(forms.ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'
        # exclude = ()