from django.db import models

# Create your models here.

#객체를 찍어내는 class만들기

class HongdaeBoardModel(models.Model):
    title=models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    body=models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] #100글자만 짤라줌


