from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse

# Create your views here.
def index2(request):
    return HttpResponse("Olla from notifications")

def index(request):
    return HttpResponsePermanentRedirect(reverse('reservations:show_form'))