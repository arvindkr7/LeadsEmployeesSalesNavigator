from django.contrib import admin

from .forms import HomeEmployeeForm, HomeLeadForm
from .models import HomeEmployee, HomeLead


@admin.register(HomeLead)
class HomeLeadAdmin(admin.ModelAdmin):
    form = HomeLeadForm
    list_display = ('company_name', 'url', 'campaign_id', 'urn')


@admin.register(HomeEmployee)
class HomeEmployeeAdmin(admin.ModelAdmin):
    form = HomeEmployeeForm
    list_display = ('first_name', 'last_name', 'urn', 'lead')
