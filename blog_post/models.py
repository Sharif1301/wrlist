from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()

	def __str(self):
		return self.title
#Post class end here

class ReadList(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()

	def __str(self):
		return self.title
#RealList class end here

class WatchList(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
		
	def __str(self):
		return self.title
#WatchList class end here