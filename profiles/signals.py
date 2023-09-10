from django.contrib.auth.models import User
from profiles.models import Profile, ProfileStatus
from django.db.models.signals import post_save
from django.dispatch import receiver

#When an operations is did on user module, then send this via recevier.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(instance.username, '----created: ', created)
    if created:
        #every time we send different user, thus we use instance.
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def create_status_message(sender, instance, created, **kwargs):
    if created:
        #every time we send different user, thus we use instance.
        ProfileStatus.objects.create(user_profile=instance,
                               status_message=f'{instance.user.username} is a new user!')
