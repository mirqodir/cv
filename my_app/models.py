from django.db import models

# Create your models here.
class Comment(models.Model):
	username = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.username