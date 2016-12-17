from django import forms
from .models import *
#Write a class that will help handle the form based on our model. This helps to handle validation as well
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        # I decided to add css class from here considering the overhead of addding widget-tweaks
        widgets = {
            'fname': forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control'}),
            'lname': forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control'}),
            'email_address': forms.TextInput(attrs={'placeholder':'Email', 'class':'form-control'}),
        }