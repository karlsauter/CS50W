from django import forms
from django.core.exceptions import ValidationError
from . import util
import re

class SearchForm(forms.Form):
    q = forms.CharField(label="", required=False, max_length=100, widget=forms.TextInput(attrs={
        "class":"search",
        "placeholder":"Search Encyclopedia"
    }))

class editEntryForm(forms.Form):
    content = forms.CharField(label="Article content", max_length=1000, widget=forms.Textarea(attrs={
        "class":"content"
    }))
    

class newEntryForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100, widget=forms.TextInput(attrs={
        "class":"title"
    }))
    content = forms.CharField(label="Article content", max_length=1000, widget=forms.Textarea(attrs={
        "class":"content"
    }))
    def clean_title(self):
        title = self.cleaned_data["title"]
        if util.get_entry(title):
            raise ValidationError("This entry already exists. Choose a different title.")
        validTitle = re.compile("^[^/\\\x00-\x1F]+$")
        if not re.search(validTitle, title):
            raise ValidationError('Title can\'t contain slashes ("/" nor "\\\").')
        return title
