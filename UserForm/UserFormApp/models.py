from django.db import models

# Create your models here.
class UserDetails(models.Model):
    id = models.AutoField(primary_key=True)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    secondary_email = models.CharField(max_length=50, blank=True, null=True)
    user_company_name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    joining_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    
