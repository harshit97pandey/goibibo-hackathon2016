from django.db import models

# Create your models here.


class Orders(models.Model):
	bookingId = models.CharField(max_length=20,db_index=True)
	itemId = models.IntegerField()
	unit = models.IntegerField()
	price = models.FloatField()