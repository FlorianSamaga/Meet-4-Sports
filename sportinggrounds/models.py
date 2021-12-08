from django.db import models
from PIL import Image

class Grounds(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    street = models.CharField(max_length=80)
    postal = models.CharField(max_length=20)
    area = models.CharField(max_length=80)
    country = models.CharField(max_length=60)
    opens=models.TimeField(auto_now=False, default=None, blank=True)
    closes=models.TimeField(auto_now=False, default=None, blank=True)
    changingrooms=models.BooleanField(default=False, blank=True)
    parkingsituation=models.TextField(default=None, blank=True)
    publictransportation=models.TextField(default=None, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='sportground_pics')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['street', 'postal', 'country', 'type'], name = 'unique_ground')
        ]