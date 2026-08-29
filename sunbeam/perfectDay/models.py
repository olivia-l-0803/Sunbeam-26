from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField()
    password = models.CharField()

    def __str__(self):
        return self.username

class forumquestion(models.Model):
    authorid = models.SmallIntegerField()
    author = models.CharField()

    text= models.CharField()

class forumpost(models.Model):
    authorid = models.SmallIntegerField()
    author = models.CharField()

    questionid =  models.SmallIntegerField()

    text= models.CharField()
