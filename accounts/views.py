#coding=utf8
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth import authenticate,login,logout

def login_index(request):
    if not request.user.is_authenticated():
        return render(request,'accounts/login.html')
    else:
        return render(request,'index/index.html')

def login_account(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:  
            if user.is_active:  
                login(request,user)  
		request.session.set_expiry(14400)
                request.session['username'] = username
                return HttpResponseRedirect('/index/')
            else:  
		err = "用户没激活"
		return render(request,'accounts/login.html',{'err':err})
        else:  
	    err = "用户密码错误"
	    return render(request,'accounts/login.html',{'err':err})
    else:
        return HttpResponseRedirect('/')

def logout_account(request):
    logout(request) 
    return HttpResponseRedirect('/')
