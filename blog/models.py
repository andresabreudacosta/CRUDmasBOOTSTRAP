from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    author= models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title