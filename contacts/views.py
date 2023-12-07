from django.http import HttpResponse
from django.shortcuts import render


def contacts_home(request):
    return HttpResponse("This will be the main contacts page, showing all the user's contacts")
