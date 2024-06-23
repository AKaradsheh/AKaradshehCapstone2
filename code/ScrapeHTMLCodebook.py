import os
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

# Specify the folder containing the HTML files
folder_path = '/NHANESData/NHANES/data_docs/2003-2004a'  #'./NHANESData/NHANES/data_docs/2003-2004a'

# Create a list to store the data
all_data = []

# Iterate through all HTML files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.htm'):
        file_path = os.path.join(folder_path, filename)

        # Read the HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(content, 'html.parser')

        # Find the table of contents under "codebook"
        codebook_section = soup.find('h3', text='CodebookLinks')
        if codebook_section:
            toc = codebook_section.find_next('ul')
            if toc:
                # Extract each item from the table of contents
                for item in toc.find_all('li'):
                    all_data.append({
                        'File': filename,
                        'Item': item.text.strip()
                    })

# Create a DataFrame from the collected data
df = pd.DataFrame(all_data)

# Save the DataFrame to an Excel file
excel_path = 'codebook_contents6.xlsx'
df.to_excel(excel_path, index=False)

print(f"Data has been saved to {excel_path}")
