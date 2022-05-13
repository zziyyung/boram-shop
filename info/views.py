from django.shortcuts import render,redirect
import pandas as pd
# 전체 모델 import
from boram3.models import *
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

logger = logging.getLogger('book')


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

NTS = NovelSing.objects.all().values()
NC = NovelColor.objects.all().values()
Novelsing = pd.DataFrame(NTS)
Novelcolor = pd.DataFrame(NC)

signup = Signup.objects.all()

# 책 정보 불러오기
@csrf_exempt
def booksearch(request):
    if request.POST['booktitle']:
        booktitle = request.POST['booktitle']
    else:
        booktitle = request.POST['book']


    # 검색된 책 이름 남기기 로그
    logger.debug(booktitle)

    if (NovelTotal[NovelTotal['title']==booktitle]['title'].count()) < 1:
    # if (NovelTotal[NovelTotal['title']==booktitle]).empty:
        errormesseage = 'false'
        return redirect('/?messeage='+errormesseage)
    else:
        R = Review.objects.all().values()
        Reviews = pd.DataFrame(R)
        if (NovelTotal[NovelTotal['title']==booktitle]['title'].count()) > 1:
            ChoiceBookTotal = (NovelTotal[NovelTotal['title'] == booktitle]).head(1)
            ChoiceBookStory = (NovelStory[NovelStory['title'] == booktitle]).head(1)
        else:
            ChoiceBookTotal = NovelTotal[NovelTotal['title'] == booktitle]
            ChoiceBookStory = NovelStory[NovelStory['title'] == booktitle]
        CBTcover = ChoiceBookTotal['coverlargeurl'].iloc[0]
        CBTtitle = ChoiceBookTotal['title'].iloc[0]
        CBTauthor = ChoiceBookTotal['author'].iloc[0]
        CBTpublisher = ChoiceBookTotal['publisher'].iloc[0]
        CBTprice = ChoiceBookTotal['pricestandard'].iloc[0]

        CBSstory = ChoiceBookStory['story'].iloc[0]
        CBSreview = ChoiceBookStory['review'].iloc[0]
        CBSpiece = ChoiceBookStory['piece'].iloc[0]

        if (Reviews[Reviews['booktitle'] == booktitle]['booktitle'].count()) >1:
            ChoiceBookReview = Reviews[Reviews['booktitle'] == booktitle].head(1)
        else:
            ChoiceBookReview = Reviews[Reviews['booktitle'] == booktitle]
        CBId = list(ChoiceBookReview['userid'])
        CBRating = list(ChoiceBookReview['rating'])
        CBReview = list(ChoiceBookReview['review'])
        CBDate = list(ChoiceBookReview['timeday'])
        CBall = zip(CBId,CBRating, CBReview, CBDate)

        # 유튜브 api 재료 및 실행ss
        CBTid = ChoiceBookTotal['id'].iloc[0]
        CBTid = str(CBTid)

        noveltosing = Novelsing[Novelsing['novel'] == CBTid]
        listnoveltosing = list(noveltosing['song'])

        youtubetitle = list()
        youtubeurl = list()
        songalbumimage = list()
        songtrackname = list()
        for i in listnoveltosing[:4]:
            i = int(i)
            i +=1
            musicid = SongChart[SongChart['id'] == i]
            musicsinger = musicid['singer'].iloc[0]
            # print(musicsinger,'singer')
            musictitle = musicid['title'].iloc[0]
            # print(musictitle,'title')
            musicalbum = musicid['album_images'].iloc[0]
            songalbumimage.append(musicalbum)
            musicname = musicid['album_name'].iloc[0]
            songtrackname.append(musicname)
            searchname = musicsinger + " " + musictitle
            yt, yu = youtube_search(searchname)
            youtubetitle.append(yt)
            youtubeurl.append(yu)

        playlist = zip(youtubetitle, youtubeurl, songtrackname, songalbumimage)
        youtubedefault = youtubeurl[0]

        NC = Novelcolor[Novelcolor['novel'] == CBTid]
        Ncolor = list(NC['color'])
        colorlist = list()
        for a in Ncolor:
            a = int(a)
            a +=1
            color = Color[Color['id'] == a]
            rgb = color['rgb'].iloc[0]
            colorlist.append(rgb)

        colorthis = colorlist[0:10]

        colordefault = colorlist[0]

        if (request.session.get('username')):
            user_id = request.session.get('username')
            user = Signup.objects.get(userid=user_id)
            # print(user_id,booktitle)
            return render(request, 'booksearch.html',
                          {'userinfo': user, 'ChoiceBookTotal': ChoiceBookTotal, 'ChoiceBookStory': ChoiceBookStory,
                           'CBTcover': CBTcover, 'CBTtitle': CBTtitle, 'CBTauthor': CBTauthor,
                           'CBTpublisher': CBTpublisher, 'CBTprice': CBTprice, 'CBSstory': CBSstory,
                           'CBSreview': CBSreview, 'CBSpiece': CBSpiece, 'list': CBall, 'colorde': colordefault,
                           'colorlist': colorthis, 'playlist': playlist, 'musicdefault': youtubedefault})
        else:
            return render(request, 'booksearch.html',
                          {'ChoiceBookTotal': ChoiceBookTotal, 'ChoiceBookStory': ChoiceBookStory, 'CBTcover': CBTcover,
                           'CBTtitle': CBTtitle, 'CBTauthor': CBTauthor, 'CBTpublisher': CBTpublisher,
                           'CBTprice': CBTprice, 'CBSstory': CBSstory, 'CBSreview': CBSreview, 'CBSpiece': CBSpiece,
                           'colorde': colordefault, 'colorlist': colorthis, 'playlist': playlist,
                           'musicdefault': youtubedefault})

# 도서 리뷰
@csrf_exempt
def insertreview(request):
    if request.method == 'POST':
        booktitle2 = request.POST['forbookname']
        userid = request.POST['foruserid']
        rating = request.POST['rating']
        review = request.POST['review']
        Review.objects.create(userid=userid,booktitle=booktitle2,rating=rating,review=review,timeday=timezone.now().date())
    return redirect('/')


# 유튜브api로 노래 불러오기
def youtube_search(option):
    # DEVELOPER_KEY = "AIzaSyCWNfSQc4K4lFo7jnpMBFgQYpXNsfRDpDo"
    # DEVELOPER_KEY ="AIzaSyB82I9gRsNvJIU1skMFtAzEq4nIeym4ZWo"
    # DEVELOPER_KEY ="AIzaSyCPvPcHmyPAFS4TcjpPaCkPEclZGtFRDOA"안댐
    # DEVELOPER_KEY = 'AIzaSyCrmFLOeyOsWrtV230eeno_gxVVJzcSr6s'안댐
    DEVELOPER_KEY = 'AIzaSyAWcKzQNoHzCG3jmI94rQuzs5DX1cv1YmI'
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    videoaddres = []

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=option+ " lyrics",
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
        singtitle = option
        createurl = 'https://www.youtube.com/embed/' + videoaddres[0]  + "?autoplay=1"

    # print(createurl)

    return singtitle, createurl


if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="Google")
  argparser.add_argument("--max-results", help="Max results", default=25)
  args = argparser.parse_args()


# 노래 평가
@csrf_exempt
def insertmatchreview(request):
    if request.method == 'POST':
        booktitle4 = request.POST['reviewbooktitle2']
        userid4 = request.POST['matchreviewid2']
        rating2 = request.POST['matchrating']
        review2 = request.POST['matchreview']
        Matchreview.objects.create(userid=userid4,booktitle=booktitle4,rating=rating2,matchreview=review2,timeday=timezone.now().date())
        messeage = '평가해주셔서 감사합니다!'
        result = {'result': messeage}
        result = (json.dumps(result, cls=NumpyEncoder, indent=4, ensure_ascii=False))
    return JsonResponse(result, safe=False)


