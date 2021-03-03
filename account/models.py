from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    line_of_business = models.CharField(max_length=200)
    organisation_type = models.CharField(max_length=200)
    business_registration_number = models.CharField(max_length=200)
    email = models.EmailField()
    contact_number = models.CharField(max_length=200)
    organisation_description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'
    def __str__(self):
        return self.name

class Policy(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    premium = models.CharField(max_length=200)
    policy_number = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'policy'
        verbose_name_plural = 'policies'
    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    policies = models.ManyToManyField(Policy)
    unique_number = models.CharField(max_length=200)
    is_super = models.BooleanField(default=False)
    country = models.CharField(max_length=200)
    payment = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='users/%Y/', blank=True)

    def __str__(self):
        return f'{self.user.username}'

class Beneficiary(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='beneficiary_policies')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='beneficiaries')
    name = models.CharField(max_length=200)
    id_number = models.CharField(max_length=200)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'benefiaciary'
        verbose_name_plural = 'beneficiaries'