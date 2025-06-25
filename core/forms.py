from django import forms
from .models import LostItem, FoundItem

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['item_name', 'item_type', 'location', 'date_lost', 'contact', 'image']
        widgets = {
            'date_lost': forms.DateInput(attrs={'type': 'date'}),
        }

class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = ['item_name', 'item_type', 'location', 'date_found', 'contact', 'image']
        widgets = {
            'date_found': forms.DateInput(attrs={'type': 'date'}),
        }
