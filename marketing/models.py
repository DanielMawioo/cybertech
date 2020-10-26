from django.db import models


class Message(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
