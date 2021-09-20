# 장고에서 제공하는 user, 기본적으로 제공하는데 상속받아 재정의 해서 사용도 가능
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
# 장고에서 제공하는 cbv의 제너릭뷰
from django.views.generic import CreateView, DetailView

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

        # 반복출력 이유는.. 항상 post들어오면 반복저장
        # post완료 이후엔 get로 돌아가게끔 만들어 줘야함
        # hello_world_list=HelloWorld.objects.all()
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})# context = data꾸러미
        # post끝나면 account앱에 hello_world 로 reverse하셈
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})# context = data꾸러미

###본강의

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm #이것 또한 기본제공 확인핤것
    #성공햇다면 어디로 보낼것인가
    # 클래스형에서는 lazy사용..
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    # template에서 사용하는 유저 객체의 이름
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'