# contact/forms.py
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'border-gray-200 rounded-md p-2 w-full', 'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'border-gray-200 rounded-md p-2 w-full', 'placeholder': 'Enter your email'})
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'border-gray-200 rounded-md p-2 w-full', 'rows': 5, 'placeholder': 'Enter your message'})
    )
