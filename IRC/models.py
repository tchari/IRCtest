from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Assessment(models.Model):
	assessor = models.ForeignKey(User, unique=False)
	site = models.CharField(max_length=30)
	
	def __str__(self):
		return self.site