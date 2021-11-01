from django.urls import path
from . import views

app_name = 'acc' #앱 마다 별칭이 겹칠 수 있으므로 앱 이름으로 구분
urlpatterns = [
    path('', views.index, name = 'index'),
    path('userlogin', views.userlogin, name = 'userlogin'),
    path('userlogout', views.userlogout, name = 'userlogout'),
    path('signup', views.signup,name = 'signup'),
    path('info', views.userinfo, name = "userinfo"),
    path('userdel', views.userdel, name = "userdel"),
]
