from django.db import models

class URL(models.Model):
	url_short = models.TextField()
	url_long = models.TextField()
	status = models.TextField()
	title = models.TextField()

# Create your models here.
