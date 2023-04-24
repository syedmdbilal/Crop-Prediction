from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserImageModel(models.Model):
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return str(self.image)

