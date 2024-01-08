from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olla from reservations")

def process_form(request):
    if request.method == "POST":
        id = request.POST["id"]
        name = request.POST["name"]
        return HttpResponse("Name: {} and id: {}".format(name, id))

def show_form(request):
    return render(request, 'res_form.html')