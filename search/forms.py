from django import forms


class SearchForm(forms.Form):
    search_phrase = forms.CharField(label='Type a city', max_length=25)
