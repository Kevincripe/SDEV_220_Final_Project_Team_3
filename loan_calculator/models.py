from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# create class for Loan Calc
class LoanCalculator(models.Model):  
    down_payment = models.FloatField(default=0)
    interest_rate = models.FloatField(default=0)
    num_of_months = models.IntegerField(default=0)
    loan_amount = models.FloatField(default=0)
    published_date = models.DateTimeField(blank=True, null=True)


    # publish date
    def publish(self):
        self.published_date = timezone.now()
        self.save()

# no string return method was needed calc calc's in html
