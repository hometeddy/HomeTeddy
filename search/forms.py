__author__ = 'RUI'

from django import forms


class SearchForm(forms.Form):
    CHOICES = [('1', '1'), ('2', '2'), ('3', '3')]
    service = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())