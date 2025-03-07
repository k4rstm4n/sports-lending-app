from django import forms
from .models import Equipment

class EquipmentFilterForm(forms.Form):
    search = forms.CharField(required = False, widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Search equipment...'
    }))

    category = forms.ChoiceField(
        choices=[('', 'All Categories')] + Equipment.CATEGORY_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    condition = forms.ChoiceField(
        choices=[('', 'All Conditions')] + Equipment.CONDITION_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    min_price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Min price'
        })
    )

    max_price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Max price'
        })
    )