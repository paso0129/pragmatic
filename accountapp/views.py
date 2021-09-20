from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":
        #helloworld input 가져와
        temp = request.POST.get('hello_world_input')

        # helloworld의 새로운객체가 여기로 들어감
        new_hello_world = HelloWorld()
        # temp의 내용을 helloworld.text에 저장
        new_hello_world.text = temp
        # db에 데이터를 저장
        new_hello_world.save()
        # hello의 모든데이터ㅗ를 모두 긁어옴

        hello_world_list=HelloWorld.objects.all()
        # 반복출력 이유는..
        # return render(request, 'acoountapp/hello_world.html', context={'hello_world_list':hello_world_list})# context = data꾸러미

        return HttpResponseRedirect(reverse('accountapp:hello_world')) #account앱에 helloworld 로 reverse하셈
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'acoountapp/hello_world.html', context={'hello_world_list':hello_world_list})# context = data꾸러미
