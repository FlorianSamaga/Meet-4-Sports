from django import forms
from .models import Grounds

#per Hand nachbauen 
# Zeile 27: profile/forms
class GroundsRegisterForm(forms.ModelForm):  
    class Meta:
        model = Grounds
        fields = '__all__'


class CreateGroundForm(forms.ModelForm):
    class Meta:
        model = Grounds
        fields = ['name', 'type', 'street', 'postal', 'area', 'country', 'opens', 'closes', 'changingrooms', 'parkingsituation', 'publictransportation', 'image']

class GroundPictureForm(forms.ModelForm):
    class Meta:
        model = Grounds
        fields = ['image']
