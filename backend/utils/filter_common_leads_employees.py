import json

import pandas as pd

'''
# Read the Parquet files
df_lead = pd.read_parquet('updated_home_employee.parquet')
df_urn = pd.read_parquet('updated_home_lead.parquet')

print(df_lead['lead_id'].head(15))
print(df_urn['urn'].head(15))
# Ensure the columns are converted to the correct types if necessary
# df_lead['lead_id'] = df_lead['lead_id'].replace({',': ''}, regex=True).fillna(0).apply(lambda x: int(x) if x != '' else 0)
# df_urn['urn'] = df_urn['urn'].replace({',': ''}, regex=True).fillna(0).apply(lambda x: int(x) if x != '' else 0)

# Find the intersection of lead_id and urn
common_ids = set(df_lead['lead_id']).intersection(set(df_urn['urn']))

# Filter both DataFrames to keep only rows with common values
df_lead_filtered = df_lead[df_lead['lead_id'].isin(common_ids)]
df_urn_filtered = df_urn[df_urn['urn'].isin(common_ids)]

# Save the updated DataFrames back to Parquet files
df_lead_filtered.to_parquet('updated_employees_table.parquet')
df_urn_filtered.to_parquet('updated_leads_table.parquet')

# Print the first 15 rows of the updated DataFrames
print(df_lead_filtered['lead_id'].head(15))
print(df_urn_filtered['urn'].head(15))

'''

'''

# Function to check if a string is a valid JSON
def is_valid_json(raw_json):
    if isinstance(raw_json, str):
        try:
            json.loads(raw_json)
            return True
        except ValueError:
            return False
    elif isinstance(raw_json, dict):
        return True  # Assume it's already a parsed dictionary
    else:
        return False


# Read the Parquet files
df_lead = pd.read_parquet('updated_employees_table.parquet')
df_urn = pd.read_parquet('updated_leads_table.parquet')

# Ensure the columns are converted to the correct types if necessary
# df_lead['lead_id'] = df_lead['lead_id'].replace({',': ''}, regex=True).fillna(0).apply(lambda x: int(x) if x != '' else 0)
# df_urn['urn'] = df_urn['urn'].replace({',': ''}, regex=True).fillna(0).apply(lambda x: int(x) if x != '' else 0)

# Further filter to keep only rows with valid JSON in 'raw_json'
df_lead = df_lead[df_lead['raw_json'].apply(is_valid_json)]
df_urn = df_urn[df_urn['raw_json'].apply(is_valid_json)]

# Find the intersection of lead_id and urn
common_ids = set(df_lead['lead_id']).intersection(set(df_urn['urn']))

# Filter both DataFrames to keep only rows with common values
df_lead_filtered = df_lead[df_lead['lead_id'].isin(common_ids)]
df_urn_filtered = df_urn[df_urn['urn'].isin(common_ids)]

# Drop the 'urn' column from df_lead_filtered
df_lead_filtered = df_lead_filtered.drop(columns=['urn'])

# Save the updated DataFrames back to Parquet files
df_lead_filtered.to_parquet('updated_employees_table_raw_json.parquet')
df_urn_filtered.to_parquet('updated_leads_table_raw_json.parquet')

# Print the first 15 rows of the updated DataFrames
print(df_lead_filtered.head())
# print(df_urn_filtered.head(15))

'''

# Number of records to take
n = 10  # Adjust n as needed

# Read the updated Parquet files
df_lead_filtered = pd.read_parquet('first_n_lead_id_employees.parquet')
df_urn_filtered = pd.read_parquet('first_n_urn_leads.parquet')

# Ensure the columns are converted to the correct types if necessary
df_lead_filtered['lead_id'] = df_lead_filtered['lead_id'].astype(int)
df_urn_filtered['urn'] = df_urn_filtered['urn'].astype(int)
df_urn_filtered['n_employees'] = df_urn_filtered['n_employees'].astype(int)

# Sort both DataFrames by 'urn' in ascending order
df_urn_sorted = df_urn_filtered.sort_values(by='urn').head(n)
last_urn_value = df_urn_sorted.iloc[-1]['urn']

# Sort both DataFrames by 'lead_id' and 'urn' in ascending order
df_lead_sorted = df_lead_filtered.sort_values(by='lead_id')
df_lead_sorted = df_lead_sorted[df_lead_sorted['lead_id'].le(last_urn_value)]


# Save the updated DataFrames back to Parquet files
df_lead_sorted.to_parquet('first_n_lead_id_employees.parquet')
df_urn_sorted.to_parquet('first_n_urn_leads.parquet')
# Print the sorted and limited DataFrames
# print(df_lead_sorted)
print(df_urn_sorted['n_employees'])
