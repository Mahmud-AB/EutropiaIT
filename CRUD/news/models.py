from django.db import models

# Create your models here.
class News(models.Model):
    cover_img=models.ImageField(null=True,blank=True)
    title=models.CharField(max_length=100)
    n_details=models.TextField(max_length=1000)

    def __str__(self):
        return self.title