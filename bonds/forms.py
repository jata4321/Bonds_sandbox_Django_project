from django import forms
from .models import Bond, BondPrice

class BondForm(forms.ModelForm):
    class Meta:
        model = Bond
        fields = '__all__'
        widgets = {
            'maturity_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class BondPriceForm(forms.ModelForm):
    class Meta:
        model = BondPrice
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }