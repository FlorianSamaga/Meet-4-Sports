from django.db import models

class Grounds(models.Model):
    name = models.CharField(Sportsgroundname, max_lenght=100)
    type = models.CharField(Type, max_lenght=100)
    street = models.CharField(Street, max_lenght=80)
    postal = models.CharField(Postal, max_lenght=20)
    area = models.CharField(Area, max_length=80)
    country = models.CharField(Country, max_lenght=60)
    opens=models.TimeField(Opens, auto_now=False, default=None, required=False)
    closes=models.TimeField(Closes, auto_now=False, default=None, required=False)
    changingrooms=models.BooleanField(Changingrooms, default=False, required=False)
    changingrooms=models.BooleanField(Changingrooms, default=False, required=False)
    parkingsituation=models.TextField(Parkingsituation, default=None, required=False)
    publictransportation=models.TextField(Publictransportation, default=None, required=False)
    image = models.ImageField(default='default.jpg', upload_to='sportground_pics')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['street', 'postal', 'country', type])
        ]