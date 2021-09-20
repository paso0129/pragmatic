from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":
        #helloworld input 가져와
        temp = request.POST.get('hello_world_input')

        # helloworld의 새로운객체가 여기로 들어감
        new_hello_world = HelloWorld()
        # inp
        new_hello_world.text = temp
        # db에 데이터를 저장
        new_hello_world.save()
        return render(request, 'acoountapp/hello_world.html', context={'hello_world_output':new_hello_world})# context = data꾸러미
    else:
        return render(request, 'acoountapp/hello_world.html', context={'text':'GET METHOD!!!'})# context = data꾸러미
