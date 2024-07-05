from django import forms

from .models import HomeEmployee, HomeLead


class HomeLeadForm(forms.ModelForm):
    class Meta:
        model = HomeLead
        fields = '__all__'
    
    raw_json = forms.JSONField(widget=forms.Textarea)


class HomeEmployeeForm(forms.ModelForm):
    class Meta:
        model = HomeEmployee
        fields = '__all__'
    
    raw_json = forms.JSONField(widget=forms.Textarea)
