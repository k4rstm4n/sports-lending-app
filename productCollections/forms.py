from django import forms
from .models import Collection


# class CollectionForm(forms.ModelForm):
#     class Meta:
#         model = Collection
#         fields = ["collection_name", "collection_description", "collection_privacy"]

class CollectionFilterForm(forms.Form):
    search = forms.CharField(required = False, widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Search collections...'
    }))