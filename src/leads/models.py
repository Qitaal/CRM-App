from django.db import models
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE


"""
This is the Django build-in user class
Django prefer to build our own user (custom user)

from django.contrib.auth import get_user_model
User = get_user_model()
"""

"""
Abstract class that implement a proper auth feature
including first_name, last_name, username, password etc.
"""
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


"""
How to make choice like dropdown form
first value is the value that get stored into database
second value is the value that will displayed

SOURCE_CHOICES = (
    ('YouTube', 'YouTube'),
    ('Google', 'Google'),
    ('Newsletter', 'Newsletter'),
)

Other field model you can use

phone = models.BooleanField(default=False)
source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
profile_picture = models.ImageField(blank=True, null=True)
special_files = models.FileField(blank=True, null=True)
    """
class Lead(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(default=0)
    organization = models.ForeignKey(UserProfile, models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


"""
We don't need to specified firstname & lastname 
becous it already in AbstractUser class
"""
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, models.CASCADE)
    
    def __str__(self):
        return self.user.email


class Category(models.Model):
    name = models.CharField(max_length=30)  # New, Contacted, Converted, Unconverted
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)