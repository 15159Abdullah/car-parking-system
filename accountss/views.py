from django.shortcuts import render , redirect,HttpResponseRedirect
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from .models import *
from .helper import forget_password_email
import uuid

def admin_login(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request,email=Email , password=password)
        print(user)
        if user is not None and user.is_admin:
            login(request,user)
            return redirect('index')
        elif user is not None and not user.is_admin:
            messages.warning(request,'Invalid Account!')
        else:
            messages.warning(request,'Invalid Email or Password!')
    return render(request,'accounts/admin/admin_login.html',context={'title':'Town Foods Admin | Log In'})

def admin_logout(request):
    request.session.clear()
    logout(request)
    return redirect('admin_login')

def admin_signup(request):
    if request.method == "POST":
        names = request.POST.get("name")
        emails = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")
 
        admin = CustomUser.objects.filter(email = emails)
        if admin.exists():
            messages.warning(request,'Email Already exist!')
            return HttpResponseRedirect(request.path_info)
        elif password != re_password:
            messages.warning(request,'Password Matching Error!')
            return HttpResponseRedirect(request.path_info)
        else:
            admin = CustomUser.objects.create(username = names,email=emails,is_admin=True,is_customer =False)
            admin.set_password(password)
            admin.save()
            login(request,admin)
            return redirect('index')
    return render(request,'accounts/admin/admin_signup.html',context={'title':'Town Foods Admin | Sign Up'})

def change_password(request,token):
    dic = {}
    try:
        user_obj = CustomUser.objects.filter(forget_password_token=token).first()

        if request.method=='POST':
            pass1=request.POST.get('pass1')
            pass2=request.POST.get('pass2')
            user_id = request.POST.get('user_id')
            if user_id is None:
                messages.warning('User Id Not Found')
                return redirect('change_password')
            if pass1!=pass2:
                messages.warning('Both Password Must Be Same')
                return redirect('change_password')
            user_obj = CustomUser.objects.get(id=user_id)
            user_obj.set_password(pass1)
            user_obj.save()
            if user_obj.is_customer:
                return redirect('user_login')
            else:
                return redirect('admin_login')

        dic={"users":user_obj.id}
    except Exception as e:
        print(e)
    return render(request,'accounts/change_password.html',context=dic)
def forget_password(request):
    try:
        if request.method=='POST':
            emails = request.POST.get('email')
            print('This is email',emails)
            if not CustomUser.objects.filter(email=emails).first():
                messages.warning(request,'Email Not Found!')
                return redirect('forget_password')
            users=CustomUser.objects.get(email=emails)
            token=str(uuid.uuid4())
            users.forget_password_token=token
            users.save()
            forget_password_email(users,token)
            messages.success(request,"email is send. Please Check Your Mail Box")
            return redirect('forget_password')
    except Exception as e:
        print(e)
    return render(request,"accounts/forget_password.html")
def user_signup(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email= request.POST.get('email')
        password = request.POST.get('password')
    
        user = CustomUser.objects.filter(email = email)
        if user.exists():
            messages.warning(request,"Email Already Exist!")
            return HttpResponseRedirect(request.path_info)
        user = CustomUser.objects.create(username = name , email = email,is_admin=False,is_customer =True)
        user.set_password(password)
        user.save()
        login(request,user)
        return redirect('home')   
    return render(request,'accounts/user/user_signup.html',context={'current_page':'signup','title':'Town Foods | Customer Sign Up'})


def user_login(request):
    if request.method == "POST":
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        user = authenticate(email = Email,password = Password)
        if user is not None and user.is_customer:
            login(request,user)
            return redirect('home')  
        elif user is not None and not user.is_customer:
            messages.warning(request,'Invalid Account!')
        else:
            messages.warning(request,'Invalid Email Or Password!')
    return render(request,'accounts/user/user_login.html',context={'current_page':'login','title':'Town Foods | Customer Login'})

def user_logout(request):
    request.session.clear()
    logout(request)
    return redirect('home')

