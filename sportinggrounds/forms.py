from django import forms
from .models import Grounds

#per Hand nachbauen 
# Zeile 27: profile/forms
class GroundsRegisterForm(forms.ModelForm):  
    class Meta:
        model = Grounds
        fields = '__all__'