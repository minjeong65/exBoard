from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pic = models.ImageField(upload_to='usr')
    point = models.IntegerField(default = 0)
    comment = models.TextField(blank=True) #테이블에 속성 추가할 때 blank = True 해주기-> migraion해주기

    def getpic(self): #사진이 없는 경우
        if self.pic:
            return self.pic.url
        return "/media/no.png"