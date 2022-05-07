from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.login,name='login'), # 뷰즈의 login 경로 수정
    path('logout/',views.logout,name='logout'), # index.html 가서 주소 바꾸기
]