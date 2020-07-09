from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["isminiz", "notunuz"]
        widgets = {
            'isminiz' : forms.TextInput(
                attrs={
                    'placeholder':'İsminiz'
                }
            ),
            'notunuz' : forms.Textarea(
                attrs={ 
                    'placeholder':'Notunuz'
                }
            ),
        }
