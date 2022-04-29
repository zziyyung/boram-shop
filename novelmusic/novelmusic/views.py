from django.shortcuts import render,redirect
import pandas as pd
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from googleapiclient.discovery import build
from oauth2client.tools import argparser
import logging


# import logging
# logger = logging.getLogger('my')

# logger = logging.getLogger('logs')
# class CaseView(View):
# 	def post(self, request):
#         try:
#             logger.info("{} {} {} 200".format(request.method, request.path, request.headers['User-Agent']))
#         except KeyError:
#         logger.warning("{} {} {} 400 : KeyError".format(request.method, request.path, request.headers['User-Agent']))


# 화신
N = Novel.objects.all().values()
NS = NovelStory.objects.all().values()
M = Music.objects.all().values()
MA = MusicAlbum.objects.all().values()
ML = MusicLyrics.objects.all().values()
MS =MusicSinger.objects.all().values()
C = Color.objects.all().values()

NovelStory = pd.DataFrame(NS)
NovelTotal = pd.DataFrame(N)
SingSong = pd.DataFrame(ML)
Singer = pd.DataFrame(MS)
SongChart = pd.DataFrame()
Album = pd.DataFrame(MA)
Color = pd.DataFrame(C)


#화신
def index(request):
    newbooks = NovelTotal.sort_values(by=['pubdate'], ascending=False).head(5)
    Ntitlelist = list(newbooks['title'])
    Nbookimage = list(newbooks['coversmallurl'])
    newbooks5 = zip(Nbookimage,Ntitlelist)
    #신간리스트 타이틀은 Ntitle,북표지는 Nbookimage
    bestbooks = NovelTotal.head(10)
    Btitlelist = list(bestbooks['title'])
    Bbookimage = list(bestbooks['coversmallurl'])
    bestbooks10 = zip(Bbookimage, Btitlelist)
    #베스트 셀러는 북표지만 가져옴 (Bbooklist)

    if (request.session.get('username')):
        user_id = request.session.get('username')
        user = Signup.objects.get(userid=user_id)
        return render(request,'index.html',{'userinfo':user,'newbooks5':newbooks5,'bestbooks10':bestbooks10})
    else:
        return render(request, 'index.html', {'newbooks5':newbooks5,'bestbooks10':bestbooks10})
# 화신
@csrf_exempt
def booksearch(request):
    booktitle = request.POST['book']
    #print(booktitle)
    ChoiceBookTotal = NovelTotal[NovelTotal['title']==booktitle]
    ChoiceBookStory = NovelStory[NovelStory['title']==booktitle]
    CBTcover = ChoiceBookTotal['coverlargeurl'].iloc[0]
    CBTtitle = ChoiceBookTotal['title'].iloc[0]
    CBTauthor = ChoiceBookTotal['author'].iloc[0]
    CBTpublisher = ChoiceBookTotal['publisher'].iloc[0]
    CBTprice = ChoiceBookTotal['pricestandard'].iloc[0]

    CBSstory = ChoiceBookStory['story'].iloc[0]
    CBSreview = ChoiceBookStory['review'].iloc[0]
    CBSpiece = ChoiceBookStory['piece'].iloc[0]
    #searchsinger = 토픽['가수']
    #searchsong = 토픽['노래']


    #테이블 노래 정보




    #밑에 입력시 노래 url 가져옴
    #youtube_search(searchsinger,searchsong)
    #밑에서부터 가수랑 노래 입력시 유튜브 api로 해당 노래링크 가져옴
    youtubetitle=list()
    youtubeurl = list()
    yt,yu = youtube_search('바이브','promise U')
    youtubetitle.append(yt)
    youtubeurl.append(yu)
    playlist = zip(youtubetitle,youtubeurl)
    print(youtubeurl)
    print(youtubetitle)
    print(playlist)
    if (request.session.get('username')):
        user_id = request.session.get('username')
        user = Signup.objects.get(userid=user_id)
        return render(request, 'booksearch.html', {'userinfo': user,'ChoiceBookTotal' : ChoiceBookTotal , 'ChoiceBookStory' : ChoiceBookStory, 'CBTcover' : CBTcover, 'CBTtitle' : CBTtitle , 'CBTauthor' : CBTauthor , 'CBTpublisher' : CBTpublisher , 'CBTprice' : CBTprice , 'CBSstory' : CBSstory , 'CBSreview' : CBSreview , 'CBSpiece' : CBSpiece,'playlist':playlist})
    else:
        return render(request, 'booksearch.html', {'ChoiceBookTotal' : ChoiceBookTotal , 'ChoiceBookStory' : ChoiceBookStory, 'CBTcover' : CBTcover, 'CBTtitle' : CBTtitle , 'CBTauthor' : CBTauthor , 'CBTpublisher' : CBTpublisher , 'CBTprice' : CBTprice , 'CBSstory' : CBSstory , 'CBSreview' : CBSreview , 'CBSpiece' : CBSpiece,'playlist':playlist})

# 지영
def customer(request):
    return render(request,'customer.html')

# 지영 화신
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

# 화신 지영
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

# 재영
def mypage(request):
    if (request.session.get('username')):
        user_id = request.session.get('username')
        user = Signup.objects.get(userid=user_id)
        return render(request,'mypage.html', {'userinfo':user})
    else:
        return render(request, 'mypage.html')

# 재영 회원정보 수정 페이지
def change(request):
    if (request.session.get('username')):
        user_id = request.session.get('username')
        user = Signup.objects.get(userid=user_id)
        return render(request, 'change.html', {'userinfo':user})
    else:
        return render(request, 'change.html')

# 화신 재영 회원정보 수정페이지에서 정보 전달및 수정 기능
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

    return redirect('/mypage')

def likes(request):
    pass


# 화신
#이 밑으로는 youtube 음악 검색입니다.
def youtube_search(option1, option2):
    DEVELOPER_KEY = "AIzaSyCWNfSQc4K4lFo7jnpMBFgQYpXNsfRDpDo"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    videoaddres = []

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=option1 + " " + option2 + " lyrics",
        part="id,snippet",
        maxResults=1
    ).execute()

    videos = []
    channels = []
    playlists = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                       search_result["id"]["videoId"]))
        elif search_result["id"]["kind"] == "youtube#playlist":
            playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                          search_result["id"]["playlistId"]))
        videoaddres.append(search_result["id"]['videoId'])
        singtitle = option1 + ' ' + option2
        createurl = 'https://www.youtube.com/embed/' + videoaddres[0]

    print(createurl)

    return singtitle, createurl


if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="Google")
  argparser.add_argument("--max-results", help="Max results", default=25)
  args = argparser.parse_args()




