from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField()
    second_name = models.TextField()
    date_hire = models.DateField(default=timezone.now)
    data_fired = models.DateField()
    type_of_employment = models.TextField()
    total_cost = models.IntegerField()
    net_income = models.IntegerField()
    brut_income = models.IntegerField()
    function = models.TextField()
    sediu = models.TextField()
    def __str__(self):
        return f'{self.user.username} Employee'