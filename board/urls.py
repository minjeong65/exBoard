from django.urls import path
from . import views


app_name = 'board' #앱 마다 별칭이 겹칠 수 있으므로 앱 이름으로 구분
urlpatterns = [
    path('', views.index, name = 'index'),
    path('detail/<pk>', views.detail, name = 'detail'),
    path('create', views.create, name = 'create'),
    path('delete/<pk>', views.delete, name='delete'),
    path('update/<pk>',views.update, name = 'update'),

]
