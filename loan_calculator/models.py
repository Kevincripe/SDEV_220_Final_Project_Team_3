from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# create class
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

    # string return method
    def __str__(self):


        monthly_interest_rate = self.interest_rate / 1200
        monthly_payment = (self.loan_amount * monthly_interest_rate ) / (1-(1 + monthly_interest_rate)**(- self.num_of_months))
        total_paid = monthly_payment * self.num_of_months
        total_interest = total_paid - self.loan_amount

        return f"Monthly Payment: {monthly_payment:.2f} Total Paid: {total_paid:.2f} Total Interest Paid: {total_interest:.2f}"


