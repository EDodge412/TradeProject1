from django import forms
from .models import listing
from .models import message
from .models import payment


class ListingForm(forms.ModelForm):
    class Meta:
        model = listing
        exclude = ['user']


class messageForm(forms.ModelForm):
    class Meta:
        model = message
        exclude = '__all__'


class checkForm(forms.ModelForm):
    class Meta:
        model = payment
        exclude = ['user']
