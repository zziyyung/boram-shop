from django.shortcuts import render
import pandas as pd
from .models import Novel,Review,Signup,Likes
from django.views.decorators.csrf import csrf_exempt
from numpyencoder import NumpyEncoder
import json
from django.http import JsonResponse


N = Novel.objects.all().values()
R = Review.objects.all().values()

NovelTotal = pd.DataFrame(N)
Review = pd.DataFrame(R)


def index(request):
    newbooks = NovelTotal.sort_values(by=['pubdate'], ascending=False).head(5)
    Ntitlelist = list(newbooks['title'])
    Nbookauthor = list(newbooks['author'])
    Nbookimage = list(newbooks['coversmallurl'])
    newbooks5 = zip(Nbookimage,Ntitlelist,Nbookauthor)
    #신간리스트 타이틀은 Ntitle,북표지는 Nbookimage
    bestbooks = NovelTotal.head(10)
    Btitlelist = list(bestbooks['title'])
    Bbookauthor = list(bestbooks['author'])
    Bbookimage = list(bestbooks['coversmallurl'])
    bestbooks10 = zip(Bbookimage, Btitlelist,Bbookauthor)
    #베스트 셀러는 북표지만 가져옴 (Bbooklist)

    Topic1 = (NovelTotal[NovelTotal['dominant_topic'] == '1']).sample(n=7)
    Topic2 = (NovelTotal[NovelTotal['dominant_topic'] == '2']).sample(n=7)
    Topic3 = (NovelTotal[NovelTotal['dominant_topic'] == '3']).sample(n=7)
    Topic4 = (NovelTotal[NovelTotal['dominant_topic'] == '4']).sample(n=7)
    Topic5 = (NovelTotal[NovelTotal['dominant_topic'] == '5']).sample(n=7)
    Topic6 = (NovelTotal[NovelTotal['dominant_topic'] == '6']).sample(n=7)
    Topic7 = (NovelTotal[NovelTotal['dominant_topic'] == '7']).sample(n=7)
    Topic8 = (NovelTotal[NovelTotal['dominant_topic'] == '8']).sample(n=7)
    Topic9 = (NovelTotal[NovelTotal['dominant_topic'] == '9']).sample(n=7)
    Topic0 = (NovelTotal[NovelTotal['dominant_topic'] == '0']).sample(n=7)

    Topic0title = list(Topic0['title'])
    Topic1title = list(Topic1['title'])
    Topic2title = list(Topic2['title'])
    Topic3title = list(Topic3['title'])
    Topic4title = list(Topic4['title'])
    Topic5title = list(Topic5['title'])
    Topic6title = list(Topic6['title'])
    Topic7title = list(Topic7['title'])
    Topic8title = list(Topic8['title'])
    Topic9title = list(Topic9['title'])

    Topic0author = list(Topic0['author'])
    Topic1author = list(Topic1['author'])
    Topic2author = list(Topic2['author'])
    Topic3author = list(Topic3['author'])
    Topic4author = list(Topic4['author'])
    Topic5author = list(Topic5['author'])
    Topic6author = list(Topic6['author'])
    Topic7author = list(Topic7['author'])
    Topic8author = list(Topic8['author'])
    Topic9author = list(Topic9['author'])


    Topic0image = list(Topic0['coversmallurl'])
    Topic1image = list(Topic1['coversmallurl'])
    Topic2image = list(Topic2['coversmallurl'])
    Topic3image = list(Topic3['coversmallurl'])
    Topic4image = list(Topic4['coversmallurl'])
    Topic5image = list(Topic5['coversmallurl'])
    Topic6image = list(Topic6['coversmallurl'])
    Topic7image = list(Topic7['coversmallurl'])
    Topic8image = list(Topic8['coversmallurl'])
    Topic9image = list(Topic9['coversmallurl'])


    Topic0write = Topic0['topic_keywords'].iloc[0]
    Topic1write = Topic1['topic_keywords'].iloc[0]
    Topic2write = Topic2['topic_keywords'].iloc[0]
    Topic3write = Topic3['topic_keywords'].iloc[0]
    Topic4write = Topic4['topic_keywords'].iloc[0]
    Topic5write = Topic5['topic_keywords'].iloc[0]
    Topic6write = Topic6['topic_keywords'].iloc[0]
    Topic7write = Topic7['topic_keywords'].iloc[0]
    Topic8write = Topic8['topic_keywords'].iloc[0]
    Topic9write = Topic9['topic_keywords'].iloc[0]



    Topic0list = zip(Topic0title, Topic0image,Topic0author)
    Topic1list = zip(Topic1title, Topic1image,Topic1author)
    Topic2list = zip(Topic2title, Topic2image,Topic2author)
    Topic3list = zip(Topic3title, Topic3image,Topic3author)
    Topic4list = zip(Topic4title, Topic4image,Topic4author)
    Topic5list = zip(Topic5title, Topic5image,Topic5author)
    Topic6list = zip(Topic6title, Topic6image,Topic6author)
    Topic7list = zip(Topic7title, Topic7image,Topic7author)
    Topic8list = zip(Topic8title, Topic8image,Topic8author)
    Topic9list = zip(Topic9title, Topic9image,Topic9author)


    # {'Topic0write':Topic0write,'Topic0list':Topic0list,'Topic1write':Topic1write,'Topic1list':Topic1list,'Topic2write':Topic2write,'Topic2list':Topic2list,'Topic3write':Topic3write,'Topic4list':Topic4list,'Topic5write':Topic5write,'Topic5list':Topic5list,'Topic6write':Topic6write,'Topic6list':Topic6list,'Topic7write':Topic7write,'Topic7list':Topic7list,'Topic8write':Topic8write,'Topic8list':Topic8list,'Topic9write':Topic9write,'Topic9list':Topic9list}


    if (request.session.get('username')):
        user_id = request.session.get('username')
        user = Signup.objects.get(userid=user_id)
        return render(request,'index.html',{'userinfo':user,'newbooks5':newbooks5,'bestbooks10':bestbooks10,'Topic0write':Topic0write,'Topic0list':Topic0list,'Topic1write':Topic1write,'Topic1list':Topic1list,'Topic2write':Topic2write,'Topic2list':Topic2list,'Topic3write':Topic3write,'Topic3list':Topic3list,'Topic4write':Topic4write,'Topic4list':Topic4list,'Topic5write':Topic5write,'Topic5list':Topic5list,'Topic6write':Topic6write,'Topic6list':Topic6list,'Topic7write':Topic7write,'Topic7list':Topic7list,'Topic8write':Topic8write,'Topic8list':Topic8list,'Topic9write':Topic9write,'Topic9list':Topic9list})
    else:
        return render(request, 'index.html', {'newbooks5':newbooks5,'bestbooks10':bestbooks10,'Topic0write':Topic0write,'Topic0list':Topic0list,'Topic1write':Topic1write,'Topic1list':Topic1list,'Topic2write':Topic2write,'Topic2list':Topic2list,'Topic3write':Topic3write,'Topic3list':Topic3list,'Topic4write':Topic4write,'Topic4list':Topic4list,'Topic5write':Topic5write,'Topic5list':Topic5list,'Topic6write':Topic6write,'Topic6list':Topic6list,'Topic7write':Topic7write,'Topic7list':Topic7list,'Topic8write':Topic8write,'Topic8list':Topic8list,'Topic9write':Topic9write,'Topic9list':Topic9list})





# 일단 마이페이지 때문에 보류
@csrf_exempt
def likes(request):
    bookuserid = request.POST['userid']
    booktitlelike = request.POST['booktitle']
    booklikeimage = request.POST['bookimage']
    bookprice = request.POST['bookprice']

    # 테이블에 넣기 : get_or_create -> 있으면 가져오고 없으면 생성해라
    # Likes.objects.get_or_create(userid=bookuserid,novel_title=booktitlelike,novel_image=booklikeimage,book_price=bookprice)

    if Likes.objects.get(userid=bookuserid,novel_title=booktitlelike,novel_image=booklikeimage,book_price=bookprice):
        # ajax
        messeage = '이 책 좋아요 !'
        result = {'result': messeage}
        result = (json.dumps(result, cls=NumpyEncoder, indent=4, ensure_ascii=False))
    else:
        messeage = '이 책 좋아요!'
        result = {'result': messeage}
        result = (json.dumps(result, cls=NumpyEncoder, indent=4, ensure_ascii=False))

    return JsonResponse(result,safe=False)

@csrf_exempt
def unlikes(request):
    bookuserid2 = request.POST['deluserid']
    booktitlelike2 = request.POST['delbooktitle']
    booklikeimage2 = request.POST['delbookimage']
    bookprice2 = request.POST['delbookprice']
    Likes.objects.filter(userid=bookuserid2,novel_title=booktitlelike2,novel_image=booklikeimage2,book_price=bookprice2).delete()

    messeage2 = '좋아요가 취소되었습니다'
    result2 = {'result2': messeage2}
    result2 = (json.dumps(result2, cls=NumpyEncoder, indent=4, ensure_ascii=False))
    return JsonResponse(result2,safe=False)








