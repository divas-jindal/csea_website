from django.db import models

# Create your models here.
class feedback(models.Model):
	email = models.CharField(max_length=300)
	name = models.CharField(max_length=100)
	comment = models.CharField(max_length=600)
	def __str__(self):
		return (str(self.id)+' : '+self.name)