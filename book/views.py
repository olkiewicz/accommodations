from django.http import HttpResponse, Http404


def index(request):
    return HttpResponse("Hello, world. You can book a room.")


def details(request):
    return HttpResponse("Details")


def place_order(request):
    return HttpResponse("Place order")
