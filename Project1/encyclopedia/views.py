from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util

class SearchForm(forms.Form):
    q = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={
        "class":"search",
        "placeholder":"Search Encyclopedia"
    }))

def index(request):

    # Process search form
    if request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            search_term = form.cleaned_data["q"]
    else:
        search_term = ""
        form = SearchForm()
    
    # If there's only one result, redirect to that entry
    entries = util.search_entries(search_term)
    if len(entries) == 1:
        return HttpResponseRedirect(reverse("entry", args=entries))

    return render(request, "encyclopedia/index.html", {
        "entries": entries,
        "form": form
    })

def entry(request, title):

    # Find entry
    entry = util.get_entry(title)
    form = SearchForm()
    if not entry:
        title = "Not Found"
        entry = "This entry does not exist. Please enter a valid entry."
    
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": entry,
        "form": form
    })
