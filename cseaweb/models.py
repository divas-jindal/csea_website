from django.db import models

# Create your models here.
class feedback(models.Model):
	cemail = models.CharField(max_length=300)
	eventname = models.CharField(max_length=100)
	fback = models.CharField(max_length=600)
	