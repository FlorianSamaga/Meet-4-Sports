from django import forms
from .models import Grounds

class GroundsRegisterForm(forms.ModelForm):  
    class Meta:
        model = Grounds
        fields = '__all__'