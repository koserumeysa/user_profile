from django.contrib.auth.models import User
from profiles.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

#When an operations is did on user module, then send this via recevier.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(instance.username, '----created: ', created)
    if created:
        #every time we send different user, thus we use instance.
        Profile.objects.create(user=instance)

