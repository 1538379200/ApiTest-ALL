from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import requests
# Create your views here.

#注册页面
def sightpage(request):
    return render(request,"userpage/sightpage.html")

#登录跳转页面
def loginjump(request):
    return render(request,"userpage/loginjump.html")

#注册账号功能实现代码
def sight(request):
    account=request.POST["Susername"]
    pwd=request.POST["Spwd"]
    email=request.POST["Email"]
    User.objects.create_user(account,email,pwd)
    return render(request,"userpage/loginjump.html")

#用户账号密码ajax验证处理代码
@csrf_exempt
def usercheck(request):
    user=request.POST["username"]
    x=[]
    for i in User.objects.all():
        x.append(i.username)
    if user in x:
        result=json.loads('{"valid":false}')    #给bootstrapVilidator中的ajax验证传入判断值
    else:
        result=json.loads('{"valid":true}')
    return JsonResponse(result)

#登录页面
@csrf_exempt
def loginpage(request):
    return render(request,"userpage/loginpage.html")


#用户登录检查代码
def userlogin(request):
    accout=request.POST["account"]
    pwd=request.POST["pwd"]
    users=authenticate(request,username=accout,password=pwd)   #验证账号密码
    if users is not None:
        login(request,users)                #登录账号
        request.session['username']=accout    #给session中传入username值（不用修改数据库）
        request.session.set_expiry(0)    #关闭浏览器删除session值
        return redirect("/")
    else:
        return render(request,"userpage/loginpage.html",{"message":"账号或者密码错误"})

#退出登录代码
def loginout(request):
    logout(request)
    return redirect("/loginpage")

#必须登录才能进去的主页
@login_required(login_url="/loginpage")   #如果没有登录跳转至登录界面
def index(request):
    return render(request,"userpage/index.html")

#以下为接口测试代码
def APITest(request):

        url=request.POST["apiurl"]   #获取地址
        types=request.POST["rqsOption"]  #获取get、post类型
        params=request.POST["params"]   #获取携带的数据
        pro=request.POST["property"]   #获取text、json返回
        proName=request.POST["properName"]   #获取json判断的数据
        values=request.POST["proValue"]   #获取期望值
        print(url,params,values,proName,types,pro)
        if not params:
            req=requests.get(url)
            if pro=='text':
                message1=req.text
                result=req.text.__contains__(values)
                if result:
                    message2="txt测试通过"
                else:
                    message2="txt测试失败"
                return render(request,"userpage/index.html",{"msg2":message1,"msg1":message2})
            else:
                message1=req.text
                if req.json()["%r"%proName]=="%r"%values:
                    message2="js测试通过"
                else:
                    message2="js测试失败"
                return render(request,"userpage/index.html",{"msg2":message1,"msg1":message2})
        else:
            if types=='get':
                reqs=requests.get(url,params=params)
                if pro=='text':
                    message1=reqs.text
                    if reqs.text.__contains__(values):
                        message2="txt测试通过"
                    else:
                        message2="txt测试失败"
                    return render(request,"userpage/index.html",{"msg2":message1,"msg1":message2})
                else:
                    message1=reqs.text
                    if reqs.json()["%r"%proName]=="%r"%values:
                        message2="js测试通过"
                    else:
                        message2="js测试失败"
                    return render(request, "userpage/index.html", {"msg2": message1, "msg1": message2})
            else:
                reqs=requests.post(url,data=params)
                if pro=='text':
                    message1=reqs.text
                    if reqs.text.__contains__(values):
                        message2="txt测试通过"
                    else:
                        message2="txt测试失败"
                    return render(request, "userpage/index.html", {"msg2": message1, "msg1": message2})
                else:
                    message1=reqs.text
                    if reqs.json()["%r"%proName]=="%r"%values:
                        message2="js测试通过"
                    else:
                        message2="js测试失败"
                    return render(request, "userpage/index.html", {"msg2": message1, "msg1": message2})









