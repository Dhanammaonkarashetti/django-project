from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=60)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    unit = models.CharField(max_length=10)
    date = models.CharField(max_length=40)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
class Plan(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=50)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=10, default="")
    plan = models.CharField(max_length=50)
    joindate = models.DateField(max_length=40)
    expiredate = models.DateField(max_length=40)
    initialamount = models.CharField(max_length=10)


    def __str__(self):
        return self.name
# Payment Model
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=[
        ('card', 'Card'),
        ('upi', 'UPI'),
        ('cash', 'Cash'),
    ])
    status = models.CharField(max_length=20, choices=[
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    ])

    def _str_(self):
        return f"{self.user.username} - {self.amount} ({self.status})"


# DietPlan Model
class DietPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.plan_name} for {self.user.username}"