from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from random import choice
import markdown2
from . import util, forms

def index(request):
    
    # Process search form
    if 'q' in request.GET:
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            search_term = form.cleaned_data["q"]
            entries = util.search_entries(search_term)
            # If there's only one result, redirect to that entry
            if len(entries) == 1:
                return HttpResponseRedirect(reverse("entry", args=entries))
    else:
        entries = util.list_entries()
        form = forms.SearchForm()
    

    return render(request, "encyclopedia/index.html", {
        "searchForm": form,
        "entries": entries
    })

def entry(request, title):

    # Find entry
    entry = util.get_entry(title)
    form = forms.SearchForm()
    if not entry:
        return render(request, "encyclopedia/notfound.html", {
            "searchForm": form,
            "title": title,
        })
    
    return render(request, "encyclopedia/entry.html", {
        "searchForm": form,
        "title": title,
        "entry": entry
    })

def new(request):
    if request.method == "POST":
        form = forms.newEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", args=[title]))
    else:
        form = forms.newEntryForm()

    return render(request, "encyclopedia/new.html", {
        "searchForm": forms.SearchForm(),
        "newPageForm": form
    })

def edit(request, title):
    title = title
    entry = util.get_entry(title)
    if not entry:
        return render(request, "encyclopedia/notfound.html", {
            "searchForm": forms.SearchForm(),
            "title": title,
        })
    if request.method == "POST":
        form = forms.editEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", args=[title]))

    data = {
        "content": entry
    }
    form = forms.editEntryForm(data)
    return render(request, "encyclopedia/edit.html", {
        "searchForm": forms.SearchForm(),
        "editForm": form,
        "title": title
    })

def random(request):
    title = choice(util.list_entries())
    print(title)
    return HttpResponseRedirect(reverse("entry", args=[title]))