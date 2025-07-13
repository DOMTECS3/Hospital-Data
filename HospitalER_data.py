
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
print(f"DataFrame shape: {df.shape[1]}")
print(df.describe())
#Create full name column by combining first initial and last name
df["Patient Full Name"] = df["Patient First Inital"].astype(str) + ". " + df["Patient Last Name"].astype(str)
#Drop the original columns used to create the full name
df.drop(columns=["Patient First Inital", "Patient Last Name"], inplace=True)
#change patients CM colum
df.rename(columns={"Patients CM": "Admission Status"}, inplace=True)
print(df.columns.tolist())

# Convert the 'Admission Status' column to a categorical type       
df["Admission Status"] = df["Admission Status"].astype("category")

#Convert Date Column to Datetime
df["Patient Admission Date"] = pd.to_datetime(df["Patient Admission Date"], errors="coerce", dayfirst=True)
print(df.head())

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

# Only convert columns that still exist after previous operations
if "Patient Id" in df.columns:
    df["Patient Id"] = df["Patient Id"].astype("string")
if "Patient Admission Date" in df.columns:
    df["Patient Admission Date"] = pd.to_datetime(df["Patient Admission Date"], errors="coerce")
if "Patient Gender" in df.columns:
    df["Patient Gender"] = df["Patient Gender"].astype("category")
if "Patient Race" in df.columns:
    df["Patient Race"] = df["Patient Race"].astype("category")
# 'Patient Last Name' and 'Patient First Inital' have been dropped, so skip their conversion
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
output_file_path = "/home/domie/Desktop/HospitalER_data_cleaned1.csv"
df.to_csv(output_file_path, index=False)
print(f"Cleaned data saved to {output_file_path}")          
       

    
 