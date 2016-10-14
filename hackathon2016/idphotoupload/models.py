from django.db import models

# Create your models here.
from rest_framework import serializers

from datetime import datetime

class CheckInPhotoDB(models.Model):
    Userid = models.IntegerField(db_index=True)
    AWSPhotoUrl = models.CharField(max_length=300)
    Email = models.CharField(max_length = 60, blank=True, null=True, default ='',db_index=True)
    Mobile = models.CharField(max_length = 20, blank=True, null=True, default ='',db_index=True)
    DateCreated = models.DateTimeField(blank = True, default=datetime.now(), null = True)




class CheckInPhotoDBSerializer(serializers.Serializer):
    Userid = serializers.IntegerField(default = 0)
    AWSPhotoUrl = serializers.CharField(max_length=300, allow_blank=True)
    Email = serializers.CharField(max_length = 60, allow_blank=True)
    Mobile = serializers.CharField(max_length = 20, allow_blank=True)
    