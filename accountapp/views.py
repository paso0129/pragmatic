from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):

    if request.method == "POST":
        return render(request, 'acoountapp/hello_world.html', context={'text':'POST METHOD!!!'})# context = data꾸러미
    else:
        return render(request, 'acoountapp/hello_world.html', context={'text':'GET METHOD!!!'})# context = data꾸러미
