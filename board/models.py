from django.db import models

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=30)
    content = models.TextField()
    photo = models.ImageField(upload_to='post',blank=True, null=True)

    def summary(self):
        if len(self.content) >= 30:
            return self.content[:30] + "..."
        return self.content


    def getphoto(self): 
        if self.photo: #사진이 있는 경우
            return self.photo.url
        return "" #사진 첨부 안하는 경우