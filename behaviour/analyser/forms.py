from django import forms

from .models import RawData

class RawDataForm(forms.ModelForm):
    class Meta:
        model = RawData
        fields = '__all__'
        widgets = {
                'media': forms.ClearableFileInput(attrs={'multiple': True})
                }

class EditInteractionsForm(forms.Form):
    min_edge = forms.IntegerField(label='Minimal edge count:', initial=0) 

