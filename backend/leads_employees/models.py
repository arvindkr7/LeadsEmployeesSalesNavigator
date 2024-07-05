from django.db import models


class HomeLead(models.Model):
    linkedin_url = models.URLField(max_length=200)
    is_demo_lead = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    n_employees = models.IntegerField(null=True, blank=True)
    raw_json = models.JSONField()
    company_name = models.CharField(max_length=255)
    url = models.URLField(max_length=20)
    urn = models.IntegerField()
    campaign_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class HomeEmployee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    raw_json = models.JSONField()
    urn = models.IntegerField()
    lead = models.ForeignKey(HomeLead, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
