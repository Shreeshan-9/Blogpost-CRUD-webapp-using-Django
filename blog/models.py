from django.db import models
from django.utils import timezone # date-time that will take timezone into consideration
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  #unrestricted text
    date_posted = models.DateTimeField(default=timezone.now)
    # args -> auto_now, auto_now_add, default
    # auto_now=True -> updates the date_posted to current date-time everytime the post was updated [last modified field]
    # auto_now_add -> sets date_posted to current date-time only when the object is created, but the value can never be updated
    # default=timezone.now -> we dont want to execute the function, we just want to pass the actual funcn as default value

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # the Post model & User model will have a relationship which will be one-to-many relationship by using a Foreign Key
    # on_delete=models.CASCADE will delete a deleted user's post(s)

    def __str__(self):
        return self.title

    

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    
