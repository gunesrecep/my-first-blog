from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=64, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    sharing_date = models.DateTimeField(verbose_name="Paylaşım Tarihi")

    def __str__(self):
        return self.title
