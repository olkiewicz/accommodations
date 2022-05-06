from django.http import HttpResponse, Http404


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    # raise Http404('Bad error')