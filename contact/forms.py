from django import forms
from django.forms import ModelForm
from .models import Contact
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': '@hafele.com.cn'}),
            'po_number': forms.TextInput(attrs={'placeholder': '76543210'})
        }