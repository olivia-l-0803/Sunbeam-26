from django.db import models

class User(models.Model):
    Username = models.CharField()
    Password = models.CharField()
    
