from django.db import models

# Create your models here.
class UserDetail(models.Model):
    id = models.AutoField(primary_key=True)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    country = models.IntegerField( blank=True, null=True)
    user_company_name = models.CharField(max_length=255, blank=True, null=True)
    joining_date = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

class country(models.Model):
    id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=50)
    is_Active = models.BooleanField()

    
