from django.db import models
from django.utils import timezone
# Create your models here.
class newappmodel(models.Model):
    NEWAPP_DB_CHOICES=[
        ('ML','New Machine'),
        ('AI','New Machine'),
    ]
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=NEWAPP_DB_CHOICES)
    description=models.TextField(default='')






    def __str__(self):
        return self.name