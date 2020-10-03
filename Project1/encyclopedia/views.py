from django import forms
from django.shortcuts import render
from . import util

class SearchForm(forms.Form):
    q = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={
        "class":"search",
        "placeholder":"Search Encyclopedia"
    }))

def index(request):
    search_term = ""
    form = SearchForm()

    if request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            search_term = form.cleaned_data["q"]

    return render(request, "encyclopedia/index.html", {
        "entries": util.search_entries(search_term),
        "form": form
    })

def entry(request, title):
    entry = util.get_entry(title)
    if entry == None:
        title = "Not Found"
        entry = "This entry does not exist. Please enter a valid entry."
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": entry
    })
