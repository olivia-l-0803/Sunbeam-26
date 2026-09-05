from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField()
    password = models.CharField()

    def __str__(self):
        return self.username

class forumpost(models.Model):
    authorid = models.SmallIntegerField()
    author = models.CharField()
    text= models.CharField()

    def __str__(self):
        return f"Post by {self.author}"

class todotask(models.Model):
    authorid = models.SmallIntegerField()
    text= models.CharField()
    done = models.BooleanField(default=False)
    due = models.DateTimeField()

    def __str__(self):
        return f"User {self.authorid}: {self.text}"

class journalentry(models.Model):
    authorid = models.SmallIntegerField()
    event = models.CharField()
    text= models.CharField()
    rating = models.CharField()

    def __str__(self):
        return f"Journal entry {self.authorid}: {self.event}"
    
