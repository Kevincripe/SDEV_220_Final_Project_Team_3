from django.conf import settings
from django.db import models
from django.utils import timezone

# class for Sales leads
class SalesLead(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    comments = models.TextField(default='Customer Request')
    published_date = models.DateTimeField(blank=True, null=True)
    
    # publish date
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # string return method
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.telephone} {self.comments}"
    