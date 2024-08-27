from django import forms
from .models import Contact

class ContactForm(forms.Form):
    fullname = forms.CharField(
                               max_length = 50,
                               label='Your Name',
                               widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"Add Your Name ..."}),
                               error_messages={
                                   'required':"Doldurmag mutlegdir",
                                   'max_length': 'Name cannot be longer than 50 characters.'
                               }) 
    
    email = forms.EmailField(
        label="E-Mail Address",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
        error_messages={
            'required': 'This field is required.',
            'invalid': 'Enter a valid email address.'
        }
    )
    message = forms.CharField(
        label='Enquiry',
        widget=forms.Textarea(attrs={'class':"form-control",'placeholder': 'Your Message'}),
        error_messages={
            'required': 'This field is required.'
        }
    )

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'desgription']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Your Name ...','maxlength': '50'}) ,
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'desgription': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }
        labels = {
            'name': 'Your Name',
            'email': 'E-Mail Address',
            'desgription': 'Enquiry',
        }
        error_messages = {
            'name': {
                'required': 'Doldurmag mutlegdir',
                'max_length': 'Name cannot be longer than 50 characters.'
            },
            'email': {
                'required': 'This field is required.',
                'invalid': 'Enter a valid email address.'
            },
            'desgription': {
                'required': 'This field is required.'
            }
        }

    def clean_email(self):
         email = self.cleaned_data.get('email')
         if not '@' in email:
              self.add_error("emaili duzgun yaz")
         return email
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        desgription = cleaned_data.get('desgription')
        if name and len(name) > 20:
            self.add_error('name', 'Name cannot be longer than 20 characters.')
        if desgription and len(desgription) > 500:
            self.add_error('desgription', 'Description 500 den cox hərif gebul eləmir')
        return cleaned_data
