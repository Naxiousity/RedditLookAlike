from django.db import models
from django.contrib.auth.models import User 
from django.db.models.deletion import CASCADE

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200) #Character Field with max length of 200
    description = models.TextField(null=True, blank=True) #Database can be blank; Form can be blank 
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) #when the room was updated
    created = models.DateTimeField(auto_now_add=True) #when the room was created


    class Meta:
        ordering = ['-updated', '-created'] #descending order
 

    def __str__(self):
        return self.name



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #Database, One to Many / models.CASCADE means that deleting all the messages in the room if you delete it
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) #when the room was updated
    created = models.DateTimeField(auto_now_add=True) #when the room was created\

    class Meta:
        ordering = ['-updated', '-created'] #descending order

    def __str__(self):
        return self.body[0:50] #Only the first 50 characters can be seen in the preview of the recent activity column