"""Views."""

from django.shortcuts import render
from .forms import UnicodeTextForm
from . import unicode_util as u


def search(request):
    """Home and search."""
    if request.method == 'POST':
        form = UnicodeTextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            normalization_form = u.get_normalization_form(text)
            text = u.examen_unicode(text)
            return render(request, 'search.html', {'form': form,
                                                   'text': text,
                                                   'normalization_form': normalization_form,
                                                   'title' : 'Unicode Search',
                                                   'tagline' : 'Examine a Unicode String'})
    form = UnicodeTextForm()
    return render(request, 'home.html', {'form': form})


def tofu(request):
    """Tofu page."""
    return render(request, 'tofu.html', {'title' : 'Tofu',
                                         'tagline' : 'Not Just For Eating'})


def character(request):
    """Character page."""
    char = 'a'
    char_desc = u.get_character_description(char)
    return render(request, 'character.html', char_desc)
