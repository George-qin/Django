from django.shortcuts import render,redirect

# Create your views here.
from  .models import models
from   django.shortcuts import HttpResponse
def index(request):

    print(request.POST.get('username', ''))

    return render(request,"index.html")

from .models import person,skill
def Person(request):
    p=person.objects.all()
    #p=person.objects.all()[0:3]限制返回三个数据
    #p=person.objects.filter(pname__contains="蔡徐坤")#限制包含名字中张飞两个字的数据
    #p=person.objects.filter(pname='貂蝉')#名字为貂蝉的数据
    """
    #能够成功
    p=person.objects.get(pname="孙权")
    p.pname="孙策"
    p.page=29
    p.pcontend="我是孙权的哥哥"
    p.save()
    
    p=person.objects.all()
    for pp in p:
        print(pp.pname,end='\n')
        """

    return render(request,"person.html",{"person":p})

def form(request):
    #存,取cookies要用到HttpResponse这个对象
    res=HttpResponse()
    #res.set_cookie("george","george is a better man !")#存cookies
    #取出cookies,注意，不能关闭浏览器，如果关闭浏览器，cookies将会被清除
    cookies=request.COOKIES
    print("cookies:",cookies["george"])
    return res

def Skill(request):
    s=skill.objects.all()
    return  render(request,"skill.html",{"skill":s})

def ShowPersonSkill(request,num):
    Sk=person.objects.get(pk=num)
    skill=Sk.skill_set.all()
    return  render(request,"skill.html",{"skill":skill})

def main(request):
    #取出session渲染页面
    name=request.session.get('name',"你还没有登录")
    return render(request,"main.html",{'username':name})

def login(request):
    return render(request,"login.html")

def showmain(request):
    #从表单里面取出来了用户输入的账号，通过request.POST.get
    username = request.POST.get("username")
    print("********************username=", username)
    #通过request.session存session
    #username="秦翼飞"
    request.session['name']=username
    return redirect('http://127.0.0.1:8000/main/')
#退出登录
from django.contrib.auth import logout
def quit(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/main/')

def register(request):
    return  render(request,"register.html")

#注册模块
from .models import *
def okregister(request):

    user=request.POST.get('username')
    Pass=request.POST.get('passwd')
    uname=username()
    passwd=password()
    uname.UserName=user
    passwd.PassWord=Pass
    passwd=uname
    uname.save()
    passwd.save()
    print(user,Pass)
    return redirect('http://127.0.0.1:8000/main/')


from .models import username,password
def judge(request):
    # uu=username.objects.all()
    # for u in uu:
    #     u=username.objects.get(pk=1)
    #     p=u.password_set.get(pk=1)
    #     print(u.UserName,p.PassWord)
    user = request.POST.get("username")
    passw = request.POST.get("password")

    len=0
    P=0
    go=username.objects.all()
    ppp=username.objects.get(pk=1)
    for a in go:
        len+=1
    for i in range(1,len+1):
        u = username.objects.get(pk=i)
        p = u.password_set.get(pk=i)
        if u.UserName==user:
            if p.PassWord == passw:
                P = 1
                Ok_or_Not = "成功"
                print(u.UserName,p.PassWord)
                break
            else:
                continue
        else:
            Ok_or_Not="失败"
            continue
    print(user,passw)
    return  render(request,"judge.html",{"Ok_or_Not":Ok_or_Not,"P":P,"user":user})

def text(request):
    return render(request,'text.html')


