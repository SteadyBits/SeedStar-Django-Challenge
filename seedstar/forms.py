from django import forms
from .models import *
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'fname': forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control'}),
            'lname': forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control'}),
            'email_address': forms.TextInput(attrs={'placeholder':'Email', 'class':'form-control'}),
        }