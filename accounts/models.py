from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


#Big Users Data
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=400,null=True,blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    # Inja bayad ba tavajoh be regex doros beshe defaultesh
    likeList = models.TextField(default='0x')
    followList = models.TextField(default='0@')
    followers = models.IntegerField(default=0)
    followings = models.IntegerField(default=0)
    #profilePic = models.ImageField()
    #bio = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
        print('Profile created!')




# Each Post Model
class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='author')
    body = models.TextField(null=True)
    likesCount = models.IntegerField(default=0)
    commentsCount = models.IntegerField(default=0)
    dateCreated = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(Profile)

    #Inja bayad behtar she
    def __str__(self):
        return self.author


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    datePublished = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    #Nahve Order moghe namayesh
    class Meta:
        ordering = ['-datePublished']

    def __str__(self):
        return self.author    




