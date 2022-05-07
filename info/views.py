from django.shortcuts import render,redirect
import pandas as pd
# 전체 모델 import
from main.models import *
# 로그 수집 import
import logging
# post방식 받을 때 csrf import ( html에서 안 쓰고 views에서 사용 )
from django.views.decorators.csrf import csrf_exempt
# 유튜브 api import
from googleapiclient.discovery import build
from oauth2client.tools import argparser
# 리뷰 테이블에 넣을시 시간 import
from django.utils import timezone

from numpyencoder import NumpyEncoder
import json
from django.http import JsonResponse

logger = logging.getLogger('my')

N = Novel.objects.all().values()
NS = NovelStory.objects.all().values()
M = Music.objects.all().values()
MA = MusicAlbum.objects.all().values()
ML = MusicLyrics.objects.all().values()
MS = MusicSinger.objects.all().values()
C = Color.objects.all().values()
R = Review.objects.all().values()

NovelStory = pd.DataFrame(NS)
NovelTotal = pd.DataFrame(N)
SingSong = pd.DataFrame(ML)
Singer = pd.DataFrame(MS)
SongChart = pd.DataFrame(M)
Album = pd.DataFrame(MA)
Color = pd.DataFrame(C)
Reviews = pd.DataFrame(R)

signup = Signup.objects.all()

# 화신
@csrf_exempt
def booksearch(request):
    # if 'booktitle' in request.POST:
    #     booktitle = request.POST['booktitle']
    # else:
    #     booktitle = request.POST['book']
    if request.POST['booktitle']:
        booktitle = request.POST['booktitle']
    else:
        booktitle = request.POST['book']
    if (NovelTotal[NovelTotal['title']==booktitle]['title'].count()) < 1:
    # if (NovelTotal[NovelTotal['title']==booktitle]).empty:
        errormesseage = 'false'
        return redirect('/?messeage='+errormesseage)
    else:
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

        ChoiceBookReview = Reviews[Reviews['booktitle']==booktitle]
        CBId = list(ChoiceBookReview['userid'])
        CBReview = list(ChoiceBookReview['review'])
        CBDate = list(ChoiceBookReview['timeday'])
        CBall = zip(CBId,CBReview,CBDate)

        # id == sing['id']
        #searchsinger = 토픽['가수']
        #searchsong = 토픽['노래']


        #테이블 노래 정보

        #밑에 입력시 노래 url 가져옴
        #youtube_search(searchsinger,searchsong)
        #밑에서부터 가수랑 노래 입력시 유튜브 api로 해당 노래링크 가져옴
        # youtubetitle=list()
        # youtubeurl = list()
        #yt,yu = youtube_search('바이브','promise U')
        # youtubetitle.append(yt)
        # youtubeurl.append(yu)
        # playlist = zip(youtubetitle,youtubeurl)
        # youtubedefault = youtubeurl[0]
        # print(youtubeurl)
        # print(youtubetitle)
        # print(playlist)
        if (request.session.get('username')):
            user_id = request.session.get('username')
            user = Signup.objects.get(userid=user_id)
            print(user_id,booktitle)
            return render(request, 'booksearch.html',
                              {'userinfo': user, 'ChoiceBookTotal': ChoiceBookTotal, 'ChoiceBookStory': ChoiceBookStory,
                               'CBTcover': CBTcover, 'CBTtitle': CBTtitle, 'CBTauthor': CBTauthor,
                               'CBTpublisher': CBTpublisher, 'CBTprice': CBTprice, 'CBSstory': CBSstory,
                               'CBSreview': CBSreview, 'CBSpiece': CBSpiece, 'list': CBall})
        else:
            return render(request, 'booksearch.html', {'ChoiceBookTotal' : ChoiceBookTotal , 'ChoiceBookStory' : ChoiceBookStory, 'CBTcover' : CBTcover, 'CBTtitle' : CBTtitle , 'CBTauthor' : CBTauthor , 'CBTpublisher' : CBTpublisher , 'CBTprice' : CBTprice , 'CBSstory' : CBSstory , 'CBSreview' : CBSreview , 'CBSpiece' : CBSpiece})#,'playlist':playlist,'musicdefault':youtubedefault})

#화신
@csrf_exempt
def insertreview(request):
    if request.method == 'POST':
        print('받음')
        booktitle2 = request.POST['forbookname']
        userid = request.POST['foruserid']
        rating = request.POST['rating']
        review = request.POST['review']
        print(booktitle2,userid,rating,review)
        Review.objects.create(userid=userid,booktitle=booktitle2,rating=rating,review=review,timeday=timezone.now().date())
        return redirect('/')


def youtube_search(option1, option2):
    # DEVELOPER_KEY = "AIzaSyCWNfSQc4K4lFo7jnpMBFgQYpXNsfRDpDo"
    DEVELOPER_KEY = 'AIzaSyCrmFLOeyOsWrtV230eeno_gxVVJzcSr6s'
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
        createurl = 'https://www.youtube.com/embed/' + videoaddres[0]  #+ "?autoplay=1"

    print(createurl)

    return singtitle, createurl


if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="Google")
  argparser.add_argument("--max-results", help="Max results", default=25)
  args = argparser.parse_args()

# 노래 평가
@csrf_exempt
def insertmatchreview(request):
    print('왔냐?')
    if request.method == 'POST':
        print('리뷰받음')
        booktitle4 = request.POST['reviewbooktitle2']
        userid4 = request.POST['matchreviewid2']
        rating2 = request.POST['matchrating']
        review2 = request.POST['matchreview']
        print(booktitle4,userid4,rating2,review2)
        Matchreview.objects.create(userid=userid4,booktitle=booktitle4,rating=rating2,matchreview=review2,timeday=timezone.now().date())
        messeage = '평가 감사합니다!'
        result = {'result': messeage}
        result = (json.dumps(result, cls=NumpyEncoder, indent=4, ensure_ascii=False))
        return JsonResponse(result, safe=False)