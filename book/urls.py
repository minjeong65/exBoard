from django.urls import path
from . import views

app_name = 'book' #앱 마다 별칭이 겹칠 수 있으므로 앱 이름으로 구분
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create', views.create, name = "create"),
    path('update/<pk>', views.update, name='update'),
    path('delete/<pk>', views.delete, name='delete'),

]
