from django.db import models

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=30)
    content = models.TextField()
    photo = models.ImageField(blank=True, null=True)

    def summary(self):
        if len(self.content) >= 30:
            return self.content[:30] + "..."
        return self.content


    def getpic(self): #사진이 없는 경우
        if self.photo:
            return self.photo.url
        return True