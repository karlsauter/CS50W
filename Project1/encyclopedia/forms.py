from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(label="", required=False, max_length=100, widget=forms.TextInput(attrs={
        "class":"search",
        "placeholder":"Search Encyclopedia"
    }))

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100, widget=forms.TextInput(attrs={
        "class":"title"
    }))
    content = forms.CharField(label="Article content", max_length=1000, widget=forms.Textarea(attrs={
        "class":"content"
    }))
