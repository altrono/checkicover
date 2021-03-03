from django.contrib import admin
from .models import Company, Policy, Member, Beneficiary

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'line_of_business', 'organisation_type','is_active', 'business_registration_number', 'email', 'contact_number', 'organisation_description']
    list_editable = ['is_active']


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'premium',
                    'policy_number', 'created']

    list_editable = ['premium']


admin.site.register(Member)




@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id_number', 'is_special']
