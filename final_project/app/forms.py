from django import forms

class LibraryForm(forms.Form):
    url = forms.URLField(label='Library URL', max_length=200)

class BookForm(forms.Form):
    url = forms.URLField(label='Book URL', max_length=200)
    text_url = forms.URLField(label='Book Text URL', max_length=200)