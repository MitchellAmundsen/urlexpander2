from django.db import models
#from datetime import datetime
from django.utils import timezone

class URL(models.Model):
	url_short = models.TextField()
	url_long = models.TextField()
	status = models.TextField()
	title = models.TextField()
	snapshot = models.TextField(default='N/A')
	recent = models.TextField(default='N/A')

# Create your models here.
