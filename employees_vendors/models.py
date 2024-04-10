from django.conf import settings
from django.db import models
from django.utils import timezone

# Class for employees and vendors
class EmployeesVendors(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200, default='None')
    business_name = models.CharField(max_length=200, default='None')
    vendor_type = models.CharField(max_length=200, default='None')

    # publish date
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # string return method
    def __str__(self):
        # Logic block to determine if employee or vendor
        if EmployeesVendors.job_title is not None:
            return f"{self.job_title} {self.first_name} {self.last_name} {self.telephone}"

        elif EmployeesVendors.business_name is not None:
            return f"{self.business_name} {self.first_name} {self.last_name} {self.telephone}"
        