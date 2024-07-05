from typing import List, Optional, Union

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from ninja import NinjaAPI, Schema
from ninja.responses import JsonResponse
from pydantic import BaseModel
from rest_framework_simplejwt.tokens import RefreshToken

from .models import HomeEmployee, HomeLead

api = NinjaAPI()


class AuthSchema(BaseModel):
    username: str
    password: str


class LeadSchema(Schema):
    linkedin_url: str
    is_demo_lead: bool
    description: str
    n_employees: int
    raw_json: dict
    company_name: str
    url: str
    urn: int
    campaign_id: str


class EmployeeSchema(Schema):
    first_name: str
    last_name: str
    raw_json: dict
    urn: int


class LeadSearchFilters(Schema):
    description: Optional[str] = None
    company_name: Optional[str] = None
    url: Optional[str] = None
    urn: Optional[str] = None
    is_demo_lead: Optional[bool] = None
    raw_json: Optional[dict] = None


class EmployeeSearchFilters(Schema):
    name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    raw_json: Optional[dict] = None


class SearchFilters(Schema):
    s_type: Optional[str] = 'all'
    keyword: Optional[str] = None


@api.post("/register")
def register(request, data: AuthSchema):
    if User.objects.filter(username=data.username).exists():
        return JsonResponse({'message': 'Username already taken'}, status=400)

    user = User.objects.create_user(username=data.username, password=data.password)
    user.save()

    return JsonResponse({'message': 'User registered successfully'}, status=201)


@api.post("/login")
def login(request, data: AuthSchema):
    user = None
    if User.objects.filter(username=data.username).exists():
        user = authenticate(username=data.username, password=data.password)
    if user:
        refresh = RefreshToken.for_user(user)
        return JsonResponse({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=200)
    return JsonResponse({"error": "Invalid credentials"}, status=401)


@api.post("/leads", response=List[LeadSchema], summary="Returns list of Leads", description="Returns a list of Leads based on filter params if provided")
def list_leads(request, filters: LeadSearchFilters):
    leads = HomeLead.objects.all()
    company_name = filters.company_name
    description = filters.description
    url = filters.url
    urn = filters.urn
    is_demo_lead = filters.is_demo_lead
    raw_json_filters = filters.raw_json
    if company_name:
        leads = leads.filter(company_name__icontains=company_name)
    if is_demo_lead:
        leads = leads.filter(is_demo_lead=is_demo_lead)
    if description:
        leads = leads.filter(description__icontains=description)
    if url:
        leads.filter(Q(url__icontains=url) | Q(linkedin_url__icontains=url))
    if urn:
        leads = leads.filter(urn=int(urn))

    if raw_json_filters:
        for key, value in raw_json_filters.items():
            lead_filter_param = {f"raw_json__{key}__icontains": value}
            leads = leads.filter(**lead_filter_param)

    return leads


@api.post("/employees", response=List[EmployeeSchema], summary="Returns list of Employees", description="Returns a list of Employees based on filter params if provided")
def list_employees(request, filters: EmployeeSearchFilters):
    employees = HomeEmployee.objects.all()
    name = filters.name
    first_name = filters.first_name
    last_name = filters.last_name
    raw_json = filters.raw_json
    if name:
        employees = employees.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
    if first_name:
        employees = employees.filter(first_name__icontains=first_name)
    if last_name:
        employees = employees.filter(last_name__icontains=last_name)
    if raw_json:
        for key, value in raw_json.items():
            employee_filter_param = {f"raw_json__{key}__icontains": value}
            employees = employees.filter(**employee_filter_param)
    return employees


@api.post("/search", response=List[Union[LeadSchema, EmployeeSchema]], summary="Searches for leads and employees", description="Returns a list of Leads, and/or Employees too based on keyword and s_type ['all', 'leads', 'employees'] provided")
def search_employees(request, filters: SearchFilters):
    s_type = getattr(filters, 's_type')
    keyword = getattr(filters, 'keyword')
    if s_type == 'leads':
        leadSearchFilter = LeadSearchFilters()
        leadSearchFilter.company_name = keyword
        leads = list_leads(request, leadSearchFilter)
        return [LeadSchema.from_orm(lead) for lead in leads]
    elif s_type == 'employees':
        empSearchFilter = EmployeeSearchFilters()
        empSearchFilter.name = keyword
        employees = list_employees(request, empSearchFilter)
        return [EmployeeSchema.from_orm(employee) for employee in employees]
    else:
        # Search across both leads and employees
        leadSearchFilter = LeadSearchFilters()
        leadSearchFilter.company_name = keyword
        empSearchFilter = EmployeeSearchFilters()
        empSearchFilter.name = keyword
        leads = list_leads(request, leadSearchFilter)
        employees = list_employees(request, empSearchFilter)
        combined_results = [LeadSchema.from_orm(lead) for lead in leads] + [EmployeeSchema.from_orm(employee) for employee in employees]
    
        return combined_results

