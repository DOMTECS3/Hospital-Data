
import pandas as pd
import numpy as np

# Set the file path to the CSV file
file_path = "/home/domie/Desktop/Hospital ER_Data.csv"

# Load the Excel file
df = pd.read_csv(file_path)

#Display the first few rows
print("Data loaded successfully") 
print(df.head())

# Display the shape of the DataFrame
print(f"DataFrame shape: {df.shape}")

# Get the number of missing data points per column
missing_data = df.isnull().sum()
print("Missing data points per column:")
print(missing_data) 

missing_percent = (df["Department Referral"].isnull().sum() / len(df["Department Referral"])) * 100
print(f"Missing values in 'Department Referral': {missing_percent:.2f}%")   

missing_percent = (df["Patient Satisfaction Score"].isnull().sum() / len(df["Patient Satisfaction Score"])) * 100
print(f"Missing values in 'Patient Satisfaction Score': {missing_percent:.2f}%")  

#Fill Department Referral with 'Unknown'
df["Department Referral"] = df["Department Referral"].fillna("Unknown")
# Drop Patient Satisfaction Score column
df.drop(columns=["Patient Satisfaction Score"], inplace=True)   

print(df.shape)
missing_data = df.isnull().sum()
print("Missing data points per column:")
print(missing_data) 

#print(df["Column"].unique()) # checking the columns with unique values.
# Convert specific columns to appropriate data types
df["Patient Id"] = df["Patient Id"].astype("string")
df["Patient Last Name"] = df["Patient Last Name"].astype("string")      
df["Patient Admission Date"] = pd.to_datetime(df["Patient Admission Date"], errors="coerce")
df["Patient_Gender"] = df["Patient Gender"].astype("category")
df["Patient Race"] = df["Patient Race"].astype("category")
df["Patient First Inital"] = df["Patient First Inital"].astype("category")
print(df.dtypes) 

#Outlier detection and removal
print(df.describe())  

#check for unstandardized data
print("Checking for unstandardized data:")
for column in df.select_dtypes(include=[np.number]).columns:
    if not np.all(np.isfinite(df[column])):
        print(f"Column '{column}' contains non-finite values (NaN, Inf, -Inf).")
    else:
        print(f"Column '{column}' is standardized with finite values.") 
        
#check for invalid entries in categorical columns
categorical_columns = df.select_dtypes(include=['category', 'object']).columns
for column in categorical_columns:
    unique_values = df[column].unique()
    if len(unique_values) < 10:  # Adjust threshold as needed
        print(f"Column '{column}' has valid categorical entries: {unique_values}")
    else:
        print(f"Column '{column}' has too many unique values to display ({len(unique_values)} unique values).")

#check for final data types and structure
print("Final DataFrame structure:")
print(df.info())                  

#save the cleaned DataFrame to a new CSV file
output_file_path = "/home/domie/Desktop/HospitalER_data_cleaned.csv"
df.to_csv(output_file_path, index=False)
print(f"Cleaned data saved to {output_file_path}")          
       

    
 