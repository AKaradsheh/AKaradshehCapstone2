import pandas as pd
import re
import os

# Define the output file to save a note
output_file = os.path.join('data', 'output_file')


# Function to append text to a file
def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text + '\n')


# Function to extract description after the dash
def extract_description(text):
    parts = text.split('-', 1)
    return parts[1].strip() if len(parts) > 1 else text


# Read the CSV files
df_2003_2004 = pd.read_csv('data/20032004Codebook.csv')

df_2005_2006 = pd.read_csv('data/20052006Codebook.csv')

# Extract descriptions and create new dataframes
df_2003_2004['Description'] = df_2003_2004['Description'].apply(extract_description)
df_2005_2006['Description'] = df_2005_2006['Description'].apply(extract_description)

# Add a column to identify the source year
df_2003_2004['Year'] = '2003-2004'
df_2005_2006['Year'] = '2005-2006'

# Combine the dataframes
df_combined = pd.concat([df_2003_2004, df_2005_2006], ignore_index=True)

# Reorder columns to have Description first
columns = ['Description', 'File', 'Variable', 'Year']
df_combined = df_combined[columns]

# Remove duplicates based on Description, keeping the first occurrence
# df_combined = df_combined.drop_duplicates(subset='Description', keep='first')

# Sort by Description
df_combined = df_combined.sort_values('Description')

# Save to a new CSV file
df_combined.to_csv('data/combined_nhanes_columndataTakeTwo.csv', index=False)

print("Combined CSV file has been created successfully.")

# Append the results to the file
append_to_file(output_file, f"Combined the column descriptions code book 2003 - 2006: {df_combined}")
