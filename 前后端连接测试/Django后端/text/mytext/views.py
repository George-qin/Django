from django.shortcuts import render
import  pymysql
# Create your views here.
from  django.http import JsonResponse
from django.http import HttpResponse
from .models import User
import urllib






i=0
"""
def judge(user,password):
    # print("用户名",user)
    # print("密码", password)

    #从数据库获取数据
    len = 0
    P = 0
    go = User.objects.all()#得到数据库迭代器
    for a in go:
        len=len+1#求得数据库的总条数
    for i in range(1, len + 1):
        u = User.objects.get(pk=i)#得到单个列表
        if u.UserName == user:
            if u.PassWord == password:
                P = 1
                Ok_or_Not = "成功"
                print(u.UserName, u.PassWord,"成功")
                break
            else:
                    continue
        else:
            Ok_or_Not = "失败"
            continue
        print(user, passw)
        return render(request, "judge.html", {"Ok_or_Not": Ok_or_Not, "P": P, "user": user})
"""

#登录功能已经完成
def index(request):
    if request.method=='POST':
        user=request.POST["name"]
        password=request.POST["password"]
    # judge(user,password)
    len = 0
    P = 0
    go = User.objects.all()  # 得到数据库迭代器
    for a in go:
        len = len + 1  # 求得数据库的总条数
    for i in range(1, len + 1):
        u = User.objects.get(pk=i)  # 得到单个列表
        if u.UserName == user:
            if u.PassWord == password:
                P = 1
                Ok_or_Not = "成功"
                print(u.UserName, u.PassWord, "成功")
                data = {
                    'imformation': '你登录成功了！！！！',
                     'code': '1'
                }
                return JsonResponse(data)
                break
            else:
                continue
        else:
            Ok_or_Not = "失败"
            print('账号和密码:')
            print(u.UserName,'                  ',u.PassWord)
            print(user, '                  ', password)
            print(Ok_or_Not)
            data = {
                'imformation': '你的账号或者密码不对！！！！',
                'code':'0'
            }
            continue
        print(user, password)
        return HttpResponse("能成功连接到后端的检验登录模块！！！！")

id=0
#注册功能
def register(request):
    global id                   #全局变量，注册计数器
    id = id + 1                 #每调用一次    +1
    if request.method == 'POST':
            UserName = request.POST["name"]
            PassWord = request.POST["password"]
            Sex=request.POST["Sex"]
            Age=int(request.POST["Age"])
            Number=int(request.POST["Number"])
            Content=request.POST["Content"]
    con=pymysql.connect(host='127.0.0.1',user='root',password='qin822197982',database='python_mysql_text',charset='utf8')#连接数据库
    cursor=con.cursor()#获取游标
    print(cursor)
    sql = "insert into mytext_user value('%d', '%s', '%s','%s','%d','%d','%s')" %(id,UserName,PassWord,Sex,Age,Number,Content)  #sql语句
    cursor.execute(sql)#执行sql语句
    con.commit()#提交执行
    cursor.close()
    con.close()
    return HttpResponse("注册成功！")



#查看个人信息（全部）
def person(request):
    len = 0
    P = 0
    user=request.POST['user']
    print(user)
    go = User.objects.all()  # 得到数据库迭代器
    for a in go:
        len = len + 1  # 求得数据库的总条数
        data = {'UserName': '',
                'Sex': '',
                'Age': '',
                'Number': '',
                'Content': ''
                }
    for i in range(1, len + 1):
        u = User.objects.get(pk=i)  # 得到单个列表
        print(u.UserName,u.PassWord,u.Sex,u.Age,u.Number,u.Content)#输出获取得到的信息
        try:
            if user==u.UserName:
            #覆盖返回信息，未用if判断

                data={'UserName':u.UserName,
                  'Sex':u.Sex,
                  'Age': u.Age,
                  'Number':u.Number,
                  'Content':u.Content,
                      }
                return JsonResponse(data)
            else:
                continue
        except KeyError:
            print("************************************没有这个用户！****************************************")
    return HttpResponse("没有这个用户请重新输入！！")

#天气查询模块
from .text import download_data
def weather(request):
    try:
        day = request.GET.get('day')#获取日期
        city = request.GET.get('city')#获取城市
        # go=Weather('http://www.tianqihoubao.com/lishi/guilin.html')
        #print(day,city)
        Weather_Url='http://www.tianqihoubao.com/lishi/'+city+'/'+day+'.html'
        data=download_data(Weather_Url)#解析URL中的数据并提取
        print(data)
        w=data[1]#气候
        t1=data[4]
        t2 = data[5]
        wind=data[7]
        print(w,t1,t2,wind)
        Data={
            'weather':w,    #天气状况
            'temperature_hight':t1, #最高气温
            'temperature_low':t2,   #最低气温
            'wind':wind #风向以及风级
        }
        return JsonResponse(Data)#返回Json数据给小程序
    except urllib.error.HTTPError:
        print("输入的城市不正确")
        str="输入的城市不正确"
        return JsonResponse(str)


ID=0
#留言功能
from .models import LiuYan  #POST到前端提交的表单
def liulan(request):
    global ID  # 全局变量，注册计数器
    ID = ID + 1
    saying=request.POST['saying']#    POST到前端提交的表单
    Name = request.POST['name']
    print(Name,saying)
    con = pymysql.connect(host='127.0.0.1', user='root', password='qin822197982', database='python_mysql_text', charset='utf8')  # 连接数据库
    cursor = con.cursor()  # 获取游标
    sql = "insert into  mytext_liuyan value('%d','%s', '%s')" % (ID,Name, saying)  # sql语句
    cursor.execute(sql)  # 执行sql语句
    con.commit()  # 提交执行
    cursor.close()
    con.close()
    return HttpResponse("成功连接到留言功能后端")

#查看留言
from .models import LiuYan
def check(request):
    data=[]
    list=LiuYan.objects.all()
    len=0
    for l in list :
        len=len+1
    for id   in range(1,len+1):
        str=LiuYan.objects.get(pk=id)
        data.append(str.name+'                     '+str.say)
    return  JsonResponse(data)