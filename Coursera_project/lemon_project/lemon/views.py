from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime

def handler404(request, exception):
    return HttpResponseNotFound("Sorry Sergio, 404 error Wazzaa")

from django.views import View

class index_class(View):
    def get(self, request):
        return HttpResponse("Get request from class view")

def index(request):
    dt = datetime.today()
    if request.method == 'GET':
        result = 'Main index + Get '
        if 'name' in  request.GET:
            result += request.GET['name']
    result =result + str(dt)
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    msg = f"""
        <br> Path: {path}
        <br> Scheme: {scheme}
        <br> Method: {method}
        <br> Address: {address}
        <br> user agent: {user_agent}
        <br> path info: {path_info}
        """

    return HttpResponse(msg)

def users(request, name, id):
    return HttpResponse("Name: {} and id: {}".format(name, id))


def usersint(request, name, id):
    return HttpResponse("INT Name: {} and id: {}".format(name, id))