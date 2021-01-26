from django.db import models
from django.utils import timezone
# Create your models here.

class UserTable(models.Model):
    email = models.EmailField(unique=True)
    jwt_token = models.TextField()

    def __str__(self):
        return str(self.email)

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(UserTable,on_delete=models.CASCADE)