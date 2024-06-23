import pandas as pd
import os
import csv


def get_csv_column_names(folder_path):
    # Dictionary to store filenames and their column names
    file_columns = {}

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            try:
                # Read only the header of the CSV file
                df = pd.read_csv(file_path, nrows=0)
                # Store the column names
                file_columns[filename] = df.columns.tolist()
            except Exception as e:
                print(f"Error reading {filename}: {str(e)}")

    return file_columns


def save_column_names_to_csv(file_columns, output_file):
    # Find the maximum number of columns in any file
    max_columns = max(len(columns) for columns in file_columns.values())

    # Prepare the rows for the output CSV
    rows = []
    for filename, columns in file_columns.items():
        # Pad the columns list with empty strings if necessary
        padded_columns = columns + [''] * (max_columns - len(columns))
        rows.append([filename] + padded_columns)

    # Write to the output CSV file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        # Write the header
        writer.writerow(['Filename'] + [f'Column {i + 1}' for i in range(max_columns)])
        # Write the data
        writer.writerows(rows)


# Main execution
if __name__ == "__main__":
    input_folder = r"C:\Users\adlik\Documents\NHANES20032006WvesAnd2011Mortality\NHANES2003DatasetsConverted\2003-2004"  # Replace with your folder path
    output_file = r"C:\Users\adlik\Documents\NHANES20032006WvesAnd2011Mortality\column_names.csv"  # Replace with your desired output path

    file_columns = get_csv_column_names(input_folder)
    save_column_names_to_csv(file_columns, output_file)
    print(f"Column names have been saved to {output_file}")

    # input_folder = r"C:\Users\adlik\Documents\NHANES20032006WvesAnd2011Mortality\NHANES2003DatasetsConverted"  # Replace with your folder path
    # output_file = r"C:\Users\adlik\Documents\NHANES20032006WvesAnd2011Mortality"  # Replace with your desired output path

