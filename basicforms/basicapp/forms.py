from django import forms
from django.core import validators
    
class FormName(forms.Form):
    name = forms.CharField(max_length=255,)
    email = forms.EmailField(max_length=255)
    verify_email = forms.EmailField(label='Enter your Email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, 
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError('Email dont match!')


