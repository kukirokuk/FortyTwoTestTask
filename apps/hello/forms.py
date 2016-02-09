from django import forms

from .models import Contact
from .widgets import ButtonWidget


class ContactForm(forms.ModelForm):
    """
    The model for Contact model edit
    """
    button = forms.CharField(widget=ButtonWidget, required=False)

    class Meta:
        model = Contact
        fields = ['name', 'last_name', 'date_of_birth', 'bio',
                  'other_contacts', 'email', 'jabber',
                  'skype', 'other_contacts', 'image']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'datepicker'}),
        }
