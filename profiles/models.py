from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model):
    #When we delete user, it deletes the related profile.
    #When we do a query, we can use 'profile' to reach this model.
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    bio=models.CharField(max_length=200, blank=True, null=True)
    location=models.CharField(max_length=30, blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to="images/profile/%Y/%m/")

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Profiles' #Thanks to this, we can change the names on the api.

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000,1000)
                #this provides to resize the image.
                img.thumbnail(output_size)
                img.save(self.photo.path)


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='status_profile')
    status_message = models.CharField(max_length=255)
    cre_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.user_profile)
    
    class Meta:
        verbose_name_plural = 'Profile Statuses'