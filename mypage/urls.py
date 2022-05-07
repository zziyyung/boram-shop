from django.urls import path
from . import views

urlpatterns = [
    path('',views.mypage,name='mypage'),
    path('change/', views.change, name='change'),
    path('changeform/', views.change_form,name='change_form'), # change.html 에서 form 태그 주소 url로 바꿔주기
]