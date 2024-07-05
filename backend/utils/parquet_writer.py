import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Read the Parquet file into a Pandas DataFrame
table = pq.read_table('updated_home_lead.parquet')
df = table.to_pandas()


# print(df['urn'].head(15))
df = df[df.urn != '']

# Update the lead_id column
df['urn'] = df['urn'].replace({',': ''}, regex=True).fillna(0).astype(int)

# Drop duplicate rows based on the 'urn' column, keeping only the first occurrence
df = df.drop_duplicates(subset='urn', keep='first')
# print('##################')
# print(df['urn'].head(15))
# Write the updated DataFrame back to a Parquet file
table = pa.Table.from_pandas(df)
pq.write_table(table, 'updated_home_lead.parquet')
