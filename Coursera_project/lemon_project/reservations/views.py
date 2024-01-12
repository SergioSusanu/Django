from django.shortcuts import render
from . import forms

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olla from reservations")

def process_form(request):
    if request.method == "POST":
        form = forms.ReservationForm(request.POST)
        if form.is_valid():
            # send to database
            form.save()
            # show thank you page
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            return render(request, 'thank_you.html',{'name': name, 'date': date} )
        return HttpResponse("Form not valid")
    return HttpResponse("Something wrong")

def show_form(request):
    f = forms.ReservationForm()
    return render(request, 'res_form.html', {'form':f})