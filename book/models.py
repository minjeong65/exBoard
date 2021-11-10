from django.db import models

# Create your models here.
class Book(models.Model):
    site_name = models.CharField(max_length=30)
    site_url = models.TextField()

    def __str__(self):
        return self.site_name

class Read(models.Model):
    read_url = models.TextField()
    title = models.CharField(max_length=100,null = True)

    def summary(self):
        if len(self.read_url) >= 75:
            return self.read_url[:75] + "..."
        return self.read_url
    
    def t_summary(self):
        if len(self.title) >= 39:
            return self.title[:39] + "..."
        return self.title