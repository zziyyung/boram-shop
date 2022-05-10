from django.shortcuts import render,redirect
from boram3.models import Signup
# 비밀번호 암호화
from django.contrib.auth.hashers import make_password, check_password
# 로그 수집 import
import logging
logger = logging.getLogger('visitor')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        userID = request.POST['userID']
        userPW = request.POST['userPW1']
        userName = request.POST['userName']
        userbirthDay = request.POST['userbirthDay']
        userGender = request.POST['userGender']
        userEmail = request.POST['userEmail']
        userPhone = request.POST['userPhone']

        Signup.objects.create(userid=userID, userpw=make_password(userPW), username=userName,
                              userbirthday=userbirthDay, useremail=userEmail, usergender=userGender,
                              userphone=userPhone,role='user')
        return redirect('/signup/login')

def login(request):
    # return render(requests,'index.html',{'userinfo':users})
    if request.method == 'POST':
        userid = request.POST['username']
        userpw = request.POST['password']



        if userid and userpw:
            if not Signup.objects.filter(userid=userid).exists():
                errMsg = "아이디를 확인해주세요"
                return render(request, 'login.html',{'errorid':errMsg})

            elif userid and userpw:
                user = Signup.objects.get(userid=userid)

            # if userPW == user.userPW:
                if check_password(userpw, user.userpw):
                    print(userpw, user)
                    request.session['username'] = user.userid
                    # return render(request,'index.html',{'userinfo':user})
                    return redirect('/')
                elif not check_password(userpw, user.userpw):
                    errMsg2 = "비밀번호를 확인해주세요"
                    return render(request, 'login.html', {'errorid': errMsg2})
    else:
        return render(request, 'login.html')


def logout(requests):
    del requests.session['username']
    return redirect('/')
