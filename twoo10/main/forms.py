from django import forms

from .models import GENDER_CHOICES


class CustomerForm(forms.Form):
    name = forms.CharField(label='Vaše jméno', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', "id": "nameInput"}))
    surname = forms.CharField(label='Vaše příjmení', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', "id": "surnameInput"}))
    email = forms.EmailField(label='Váš Email', widget=forms.TextInput(
        attrs={'class': 'form-control', "id": "emailInput"}))
    date_of_birth = forms.DateField(label='Vaše datum narození', widget=forms.DateInput(
        attrs={"type": "date", 'class': 'form-control', "id": "dobInput"}))
    gender = forms.ChoiceField(label='Vaše pohlaví', choices=GENDER_CHOICES, initial="U", widget=forms.Select(
        attrs={'class': 'form-control', "id": "genderInput"}))
