# your_app/management/commands/load_parquet_data.py
import json

import pandas as pd
from django.core.management.base import BaseCommand

from leads_employees.models import HomeEmployee, HomeLead


class Command(BaseCommand):
    help = 'Load data from Parquet files into the database'

    def handle(self, *args, **kwargs):
        # self.load_leads()
        self.load_employees()
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from Parquet files'))

    def load_leads(self):
        leads_file_path = 'data/first_n_urn_leads.parquet'
        leads_df = pd.read_parquet(leads_file_path)

        # Ensure the columns are converted to the correct types if necessary
        leads_df['urn'] = leads_df['urn'].astype(int)
        leads_df['n_employees'] = leads_df['n_employees'].astype(int)
       
        for index, row in leads_df.iterrows():
            # Ensure raw_json is valid JSON
            try:
                raw_json = json.loads(row.get('raw_json', {}))
            except ValueError:
                raw_json = {}
            lead, created = HomeLead.objects.update_or_create(
                company_name=row.get('company_name_linkedin', None),
                url=row.get('url', None),
                campaign_id=row.get('campaign_id', None),
                defaults={
                    'linkedin_url': row.get('linkedin_url', None),
                    'is_demo_lead': row.get('is_demo_lead', False),
                    'description': row.get('description', ''),
                    'n_employees': int(row['n_employees']),
                    'raw_json': raw_json,
                    'urn': int(row.get('urn', 0)),
                }
            )
            lead.save()
        self.stdout.write(self.style.SUCCESS('Successfully loaded HomeLead data'))

    def load_employees(self):
        employees_file_path = 'data/first_n_lead_id_employees.parquet'
        employees_df = pd.read_parquet(employees_file_path)
        # Ensure the columns are converted to the correct types if necessary
        employees_df['lead_id'] = employees_df['lead_id'].astype(int)
        print(employees_df.head())
        for index, row in employees_df.iterrows():
            print(f'{row=}')
            if row['lead_id'] is not None:
                print(f"{row['lead_id']=}, {row['first_name']=}, {row['last_name']=} ")
                try:
                    lead = HomeLead.objects.get(urn=int(row['lead_id']))
                    if lead:
                        print('lead found', getattr(lead, 'company_name'), getattr(lead, 'urn'))
                        # print(f'{row=}')
                        try:
                            raw_json = json.loads(row.get('raw_json', {}))
                        except ValueError:
                            raw_json = {}
                        employee, created = HomeEmployee.objects.update_or_create(
                            first_name=row['first_name'],
                            last_name=row['last_name'],
                            lead=lead,
                            defaults={
                                'first_name': row['first_name'],
                                'last_name': row['last_name'],
                                'raw_json': raw_json,
                                'urn': row.get('urn', 0),
                            }
                        )
                        print('employee created', getattr(employee, 'first_name'), getattr(employee, 'last_name'))
                        employee.save()
                        self.stdout.write(self.style.SUCCESS('Successfully saved HomeEmployee data'))
                    else:
                        self.stdout.write(self.style.WARNING(f"Lead with urn {row['lead_id']} does not exist. Skipping employee."))
                except HomeLead.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Lead with urn {row['lead_id']} does not exist. Skipping employee."))
                except HomeEmployee.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Employee matching query does not exist. Skipping employee entry with lead_id {row['lead_id']}."))
            else:
                self.stdout.write(self.style.WARNING("lead_id is None. Skipping employee."))
            self.stdout.write(self.style.SUCCESS('Successfully loaded HomeEmployee data'))