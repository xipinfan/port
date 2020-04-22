from django.db import models

# Create your models here.

class Gallery(models.Model):
    description = models.CharField(max_length=100, verbose_name="概述")
    image = models.ImageField(default='defaule.png', upload_to='mage/')
    title = models.CharField(max_length=50, default='作品标题')
    def __str__(self):
        return self.title
