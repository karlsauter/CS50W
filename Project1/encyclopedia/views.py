from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util, forms

def index(request):
    
    # Process search form
    if 'q' in request.GET:
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            search_term = form.cleaned_data["q"]
    else:
        search_term = ""
        form = forms.SearchForm()
    
    # If there's only one result, redirect to that entry
    entries = util.search_entries(search_term)
    if len(entries) == 1:
        return HttpResponseRedirect(reverse("entry", args=entries))

    return render(request, "encyclopedia/index.html", {
        "searchForm": form,
        "entries": entries
    })

def entry(request, title):

    # Find entry
    entry = util.get_entry(title)
    form = forms.SearchForm()
    if not entry:
        title = "Not Found"
        entry = "This entry does not exist. Please enter a valid entry."
    
    return render(request, "encyclopedia/entry.html", {
        "searchForm": form,
        "title": title,
        "entry": entry
    })

def newpage(request):
    return render(request, "encyclopedia/newpage.html", {
        "searchForm": forms.SearchForm(),
        "newPageForm": forms.NewPageForm()
    })