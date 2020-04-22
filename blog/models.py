from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(verbose_name='标题', max_length=50)
    date = models.DateField(verbose_name='时间')
    image = models.ImageField(default='default.png', verbose_name='演示图片', upload_to='mage/')
    text = models.TextField(verbose_name='正文')

    def __str__(self):
        return self.title
