from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # creates a one-to-one relation with User model
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.user.username} Profile \n Bio: {self.bio}'

    
    def save(self):
        # this save() gets run after our model is saved
        
        super().save() # running the same save() from parent class
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) #resize & save
            img.save(self.image.path)
