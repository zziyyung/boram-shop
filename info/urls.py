from django.urls import path
from . import views

urlpatterns = [
    path('',views.booksearch,name='booksearch'),
    path('insertreview/',views.insertreview,name='insertreview'), # booksearch 에서 review form태그 url로 바꾸기
    path('insertmatchreview/',views.insertmatchreview,name='insertmatchreview'), # 경로 잘 바꿔주기
]