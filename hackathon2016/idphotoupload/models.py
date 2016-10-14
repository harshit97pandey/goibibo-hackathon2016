from django.db import models

# Create your models here.
from rest_framework import serializers

from datetime import datetime

class CheckInPhotoDB(models.Model):
    Userid = models,IntField(default = 0)
    AWSPhotoUrl = models.TextField()
    Email = models.CharField(max_length = 60)
    Mobile = models.CharField(max_length = 20)
    DateCreated = models.DateTimeField(blank = True, default=datetime.now(), null = True)




class CheckInPhotoDBSerializer(serializers.Serializer):
    Userid = serializers,IntField(default = 0)
    AWSPhotoUrl = serializers.TextField()
    Email = serializers.CharField(max_length = 60)
    Mobile = serializers.CharField(max_length = 20)
    DateCreated = serializers.DateTimeField(blank = True, null = True, default=datetime.now())