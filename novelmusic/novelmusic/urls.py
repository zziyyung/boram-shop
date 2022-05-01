"""novelmusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('booksearch/',views.booksearch,name='booksearch'),
    path('customer/',views.customer,name='customer'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('mypage/',views.mypage,name='mypage'),
    path('logout/',views.logout,name='logout'),
    path('change/', views.change, name='change'),
    path('changeform/', views.change_form,name='change_form'),
    path('likes/', views.likes, name='likes'),
]

