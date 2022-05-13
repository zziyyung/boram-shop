from django.shortcuts import render,redirect
from boram3.models import Signup,Likes
from django.contrib.auth.hashers import make_password
import pandas as pd


def mypage(request):
    L = Likes.objects.all().values()
    Likespd = pd.DataFrame(L)
    if (request.session.get('username')):
        user_id = request.session.get('username')
        user = Signup.objects.get(userid=user_id)
        if (Likespd[Likespd['userid']==user_id]['userid'].count()) < 1:
            return render(request, 'mypage.html', {'userinfo': user})
        else:
            liketable = Likespd[Likespd['userid']==user_id]
            likebooktitle = list(liketable['novel_title'])
            likebookimage = list(liketable['novel_image'])
            likebookprice = list(liketable['book_price'])
            #print(likebookprice)
            likeallthing = zip(likebookimage,likebooktitle,likebookprice)
            return render(request,'mypage.html', {'userinfo':user,'liketable': likeallthing})
    else:
        return render(request, 'mypage.html')

def change(request):
    if (request.session.get('username')):
        user_id = request.session.get('username')
        user = Signup.objects.get(userid=user_id)
        return render(request, 'change.html', {'userinfo':user}) # 주소 맞음
    else:
        return render(request, 'change.html') # 주소 맞음

def change_form(request):

    userID = request.POST['userID']
    userPW = request.POST['userPW1']
    userName = request.POST['userName']
    userbirthDay = request.POST['userbirthDay']
    userGender = request.POST['userGender']
    userEmail = request.POST['userEmail']
    userPhone = request.POST['userPhone']

    change = Signup.objects.filter(userid=userID)

    change_password = change.update(userpw=make_password(userPW))
    change_name = change.update(username=userName)
    change_birthday = change.update(userbirthday=userbirthDay)
    change_gender = change.update(usergender=userGender)
    change_email = change.update(useremail=userEmail)
    change_phone = change.update(userphone=userPhone)

    return redirect('/mypage') # 주소 맞음 ( 다시 마이페이지로 돌아가기 )
