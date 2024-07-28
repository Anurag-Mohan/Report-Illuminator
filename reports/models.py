from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class ConversionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversion_type = models.CharField(max_length=100)  
    result = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, default='DefaultFirstName')
    last_name = models.CharField(max_length=30, default='DefaultLastName')
    age = models.IntegerField(default=0)
    dob = models.DateField(default='1970-01-01')

    def __str__(self):
        return self.user.username