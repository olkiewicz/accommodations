from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from search import SearchEngine
from search.forms import SearchForm


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            search_phrase = form.cleaned_data['search_phrase']
            return HttpResponseRedirect(f'results/{search_phrase}')

    else:
        form = SearchForm()

    template = loader.get_template('search/index.html')
    context = {
        'some_text': 'You can search for a room.',
        'form': form
    }

    return HttpResponse(template.render(context, request))


def results(request, search_phrase):
    template = loader.get_template('search/results.html')
    search_results = SearchEngine.get_results(search_phrase)
    context = {
        'some_text': 'Results.',
        'search_results': search_results
    }

    return HttpResponse(template.render(context, request))
