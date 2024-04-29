from django.conf import settings
from django.db import models
from django.utils import timezone

# class for Sold Vehicles
class SoldUnits(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Inventory = models.CharField(max_length=200)
    Year_Make_Model = models.CharField(max_length=200)
    comments = models.TextField(default='Customer Request')
    published_date = models.DateTimeField(blank=True, null=True)
    
    # publish date
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # string return method
    def __str__(self):
        return f"{self.Inventory} {self.Year_Make_Model} {self.comments}"
    