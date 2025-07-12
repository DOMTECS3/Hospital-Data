
import pandas as pd
import numpy as np

# Set the file path to the CSV file
file_path = "/home/domie/Desktop/Hospital ER_data.csv"

# Load the Excel file
df = pd.read_csv(file_path)

#Display the first few rows
print("Data loaded successfully") 
print(df.head())

# # Display the shape of the DataFrame
# print(f"DataFrame shape: {df.shape}")

# # Get the number of missing data points per column
# missing_data = df.isnull().sum()
# print("Missing data points per column:")
# print(missing_data) 

# #total missing values   
# total_missing = missing_data.sum()
# print(f"Total missing values in the dataset: {total_missing}")      

# #total number of cells in the dataset
# total_cells = np.prod(df.shape)
# total_missing_percentage = (total_missing / total_cells) * 100
# print(f"Percentage of missing values in the dataset: {total_missing_percentage:.2f}%    ")    

# #drop columns with more than 50% missing values
# threshold = 0.5 * df.shape[0]
# columns_to_drop = df.columns[df.isnull().sum() > threshold]
# df.drop(columns=columns_to_drop, inplace=True)
# print(f"Dropped columns with more than 50% missing values: {columns_to_drop.tolist()}")         

# print(df.shape)
# # check for data types of each column
# print("Data types of each column:")
# print(df.dtypes)    

# #print(df["Column"].unique()) # checking the columns with unique values.
# # Convert specific columns to appropriate data types
# df["Patient Id"] = df["Patient Id"].astype("string")
# df["Patient Last Name"] = df["Patient Last Name"].astype("string")      
# df["Patient Admission Date"] = pd.to_datetime(df["Patient Admission Date"], errors="coerce")
# df["Patient_Gender"] = df["Patient Gender"].astype("category")
# df["Patient Race"] = df["Patient Race"].astype("category")
# df["Patient First Inital"] = df["Patient First Inital"].astype("category")
# print(df.dtypes) 

# #Outlier detection and removal
# print(df.describe())  

# #check for unstandardized data
# print("Checking for unstandardized data:")
# for column in df.select_dtypes(include=[np.number]).columns:
#     if not np.all(np.isfinite(df[column])):
#         print(f"Column '{column}' contains non-finite values (NaN, Inf, -Inf).")
#     else:
#         print(f"Column '{column}' is standardized with finite values.") 
        
# #check for invalid entries in categorical columns
# categorical_columns = df.select_dtypes(include=['category', 'object']).columns
# for column in categorical_columns:
#     unique_values = df[column].unique()
#     if len(unique_values) < 10:  # Adjust threshold as needed
#         print(f"Column '{column}' has valid categorical entries: {unique_values}")
#     else:
#         print(f"Column '{column}' has too many unique values to display ({len(unique_values)} unique values).")

# #check for final data types and structure
# print("Final DataFrame structure:")
# print(df.info())                  

# #save the cleaned DataFrame to a new CSV file
# output_file_path = "/home/domie/Desktop/Hospital_data_cleaned.csv"
# df.to_csv(output_file_path, index=False)
# print(f"Cleaned data saved to {output_file_path}")          
       

    
 