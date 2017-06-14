from django.db import models

class Post(models.Model):
	username = models.CharField(max_length=50)
	post_date = models.DateTimeField(auto_now_add=True)
	comment = models.CharField(max_length=140)
