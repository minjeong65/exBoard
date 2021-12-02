from django.db import models
from django.utils import timezone
from acc.models import User


# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=30)
    content = models.TextField()
    photo = models.ImageField(upload_to='post',blank=True, null=True)
    ctime = models.DateTimeField()
    voter = models.ManyToManyField(User)
    
    
    def sub_summary(self):
        if len(self.subject) >= 25:
            return self.subject[:25] + "..."
        return self.subject

    def summary(self):
        if len(self.content) >= 20:
            return self.content[:20] + "..."
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