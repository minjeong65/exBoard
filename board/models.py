from django.db import models
from django.utils import timezone


# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=30)
    content = models.TextField()
    photo = models.ImageField(upload_to='post',blank=True, null=True)
    ctime = models.DateTimeField()
    
    
    def summary(self):
        if len(self.content) >= 30:
            return self.content[:30] + "..."
        return self.content


    def getphoto(self): 
        if self.photo: #사진이 있는 경우
            return self.photo.url
        return "" #사진 첨부 안하는 경우

    
class Reply(models.Model):
    sub = models.ForeignKey(Board, on_delete = models.CASCADE)
    replyer = models.CharField(max_length=50)
    comment = models.TextField(blank=True)
    create_time = models.DateTimeField()