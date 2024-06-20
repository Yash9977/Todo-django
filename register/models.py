from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class register(models.Model):
    username=models.ForeignKey('auth.user',on_delete=models.DO_NOTHING,null=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    phone=models.IntegerField()
    address=models.TextField()