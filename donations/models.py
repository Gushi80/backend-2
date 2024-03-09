from django.db import models

# Create your models here.
class Donation(models.Model):
  amount= models.DecimalField(max_digits=10, decimal_places=2)
  donor_name= models.CharField(max_length=100)
  email=models.EmailField()
  donation_date=models.DateTimeField(auto_now_add=True)
