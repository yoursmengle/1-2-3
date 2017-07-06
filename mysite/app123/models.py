from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64)
    mobile = models.CharField(max_length=16)
    email = models.EmailField()

class Question(models.Model):
    owner = models.ForeignKey(User)
    content = models.CharField(max_length = 4096)
    create_date = models.DateField()


