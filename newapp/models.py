from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class newappmodel(models.Model):
    NEWAPP_DB_CHOICES=[
        ('ML','Machine-1'),
        ('AI','Machine-2'),
    ]
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=NEWAPP_DB_CHOICES)
    description=models.TextField(default='')

    def __str__(self):
        return self.name

class Comment(models.Model):
    newappmodel = models.ForeignKey(newappmodel, on_delete=models.CASCADE, related_name='comments')
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.User.username} on {self.newappmodel.name}'

class Self(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    app_varieties=models.ManyToManyField(newappmodel, related_name='shelves')
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return self.user.username

