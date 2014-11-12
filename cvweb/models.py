from django.db import models

# Create your models here.

class Contacto(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	website = models.URLField()
	message = models.TextField()
	date = models.DateTimeField()

	def _unicode_(self):
		return "%s %s" % (self.name, self.email)