from django.shortcuts import render,redirect
import pandas as pd
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
import csv

NovelStory=pd.read_csv('./static/data/novel_story_final.csv',encoding='utf-8')
NovelTotal=pd.read_csv('./static/data/novel_total_final.csv',encoding='utf-8')
SingSong=pd.read_csv('./static/data/singasong.csv',encoding='utf-8')
Singer=pd.read_csv('./static/data/singer.csv',encoding='utf-8')
SongChart=pd.read_csv('./static/data/songChart.csv',encoding='utf-8')
Album=pd.read_csv('./static/data/album.csv',encoding='utf-8')
Color=pd.read_csv('./static/data/newcolor1.csv',encoding='utf-8')


def index(request):
    newbooks = NovelTotal.sort_values(by=['pubDate'], ascending=False).head(5)
    Ntitlelist = list(newbooks['title'])
    Nbookimage = list(newbooks['coverSmallUrl'])
    newbooks5 = zip(Nbookimage,Ntitlelist)
    #신간리스트 타이틀은 Ntitle,북표지는 Nbookimage
    bestbooks = NovelTotal.head(10)
    Btitlelist = list(bestbooks['title'])
    Bbookimage = list(bestbooks['coverSmallUrl'])
    bestbooks10 = zip(Bbookimage, Btitlelist)
    #베스트 셀러는 북표지만 가져옴 (Bbooklist)

    if (request.session.get('username')):
        user_id = request.session.get('username')
        user = Signup.objects.get(userid=user_id)
        return render(request,'index.html',{'userinfo':user,'newbooks5':newbooks5,'bestbooks10':bestbooks10})
    else:
        return render(request, 'index.html', {'newbooks5':newbooks5,'bestbooks10':bestbooks10})

@csrf_exempt
def booksearch(request):
    booktitle = request.POST['book']
    #print(booktitle)
    ChoiceBookTotal = NovelTotal[NovelTotal['title']==booktitle]
    ChoiceBookStory = NovelStory[NovelStory['title']==booktitle]
    CBTcover = ChoiceBookTotal['coverLargeUrl'].iloc[0]
    CBTtitle = ChoiceBookTotal['title'].iloc[0]
    CBTauthor = ChoiceBookTotal['author'].iloc[0]
    CBTpublisher = ChoiceBookTotal['publisher'].iloc[0]
    CBTprice = ChoiceBookTotal['priceStandard'].iloc[0]

    CBSstory = ChoiceBookStory['story'].iloc[0]
    CBSreview = ChoiceBookStory['review'].iloc[0]
    CBSpiece = ChoiceBookStory['piece'].iloc[0]

    if (request.session.get('username')):
        user_id = request.session.get('username')
        user = Signup.objects.get(userid=user_id)
        return render(request, 'booksearch.html', {'userinfo': user,'ChoiceBookTotal' : ChoiceBookTotal , 'ChoiceBookStory' : ChoiceBookStory, 'CBTcover' : CBTcover, 'CBTtitle' : CBTtitle , 'CBTauthor' : CBTauthor , 'CBTpublisher' : CBTpublisher , 'CBTprice' : CBTprice , 'CBSstory' : CBSstory , 'CBSreview' : CBSreview , 'CBSpiece' : CBSpiece})
    else:
        return render(request, 'booksearch.html', {'ChoiceBookTotal' : ChoiceBookTotal , 'ChoiceBookStory' : ChoiceBookStory, 'CBTcover' : CBTcover, 'CBTtitle' : CBTtitle , 'CBTauthor' : CBTauthor , 'CBTpublisher' : CBTpublisher , 'CBTprice' : CBTprice , 'CBSstory' : CBSstory , 'CBSreview' : CBSreview , 'CBSpiece' : CBSpiece})


def customer(request):
    return render(request,'customer.html')


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
        return redirect('/login')


def login(request):
    # return render(requests,'index.html',{'userinfo':users})
    if request.method == 'POST':
        userid = request.POST['username']
        userpw = request.POST['password']

        if userid and userpw:
            user = Signup.objects.get(userid=userid)

            # if userPW == user.userPW:
            if check_password(userpw, user.userpw):
                print(userpw, user)
                request.session['username'] = user.userid
                # return render(request,'index.html',{'userinfo':user})
                return redirect('/')
            else:
                return redirect('/login')
    else:
        return render(request, 'login.html')


def logout(requests):
    del requests.session['username']
    return redirect('/')


def mypage(request):
    return render(request,'mypage.html')