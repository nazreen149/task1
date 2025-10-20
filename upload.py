import pandas as pd

# Load the dataset
file_path ='C:\\Users\\nazreen\\Downloads\\marketing_campaign.csv'
df =df.fillna({'Income': median_income}, inplace=True)

# 1. Check for missing values
missing_values = df.isnull().sum()
print("Missing values per column before cleaning:")
print(missing_values)

# 2. Fill missing Income values with median
median_income = df['Income'].median()
df['Income'].fillna(median_income, inplace=True)
print(f"Filled missing Income values with median: {median_income}")

# 3. Remove duplicate rows
initial_shape = df.shape
df.drop_duplicates(inplace=True)
after_drop_shape = df.shape
print(f"Dataset shape before removing duplicates: {initial_shape}")
print(f"Dataset shape after removing duplicates: {after_drop_shape}")

# 4. Standardize text values in 'Education' and 'Marital_Status'
df['Education'] = df['Education'].str.strip().str.lower()
df['Marital_Status'] = df['Marital_Status'].str.strip().str.lower()

# 5. Convert 'Dt_Customer' to datetime format
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y', errors='coerce')

# 6. Rename columns to lowercase and replace spaces with underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')

# 7. Verify and convert data types if necessary
print("Data types after cleaning:")
print(df.dtypes)

# 8. Save the cleaned dataset
output_file = 'cleaned_marketing_campaign.csv'
df.to_csv(output_file, index=False)
print(f"Cleaned dataset saved as {output_file}")
