import pyreadstat
import pandas as pd
import os

# C:\Users\adlik\Documents\NHANES20032006WvesAnd2011Mortality\NHANES2003Datasets
# C:\Users\adlik\Documents\NHANES20032006WvesAnd2011Mortality\NHANES2003DatasetsConverted
# input_folder = r"C:\path\to\your\input\folder"  # Replace with your input folder path
# output_folder = r"C:\path\to\your\output\folder"  # Replace with your output folder path
# C:\Source\CapstoneTwoHTNandParameters\NHANESData\NHANES\raw_data\2017-2018
# C:\Source\CapstoneTwoHTNandParameters\NHANESData\NHANES\raw_data\2003-2004
# C:\Source\CapstoneTwoHTNandParameters\NHANESData\NHANES\raw_data\2005-2006
# C:\Source\CapstoneTwoHTNandParameters\NHANESData\NHANES\raw_data\2013-2014

# Function to append text to a file
def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text + '\n')


def convert_xpt_to_csv(input_file, output_file):
    try:
        # Read the XPT file
        df, meta = pyreadstat.read_xport(input_file)

        # Save as CSV
        df.to_csv(output_file, index=False)
        print(f"Successfully converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error converting {input_file}: {str(e)}")


def process_folder(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # # Process each XPT file in the input folder
    # for filename in os.listdir(input_folder):
    #     if filename.endswith('.xpt'):
    #         input_path = os.path.join(input_folder, filename)
    #         output_path = os.path.join(output_folder, filename.replace('.xpt', '.csv'))
    #         convert_xpt_to_csv(input_path, output_path)

    # # Process each XPT file in the input folder
    # for filename in os.listdir(input_folder):
    #     print(f"Processing file: {filename}")
    #     if filename.endswith('.xpt'):
    #         print(f"File {filename} is an XPT file, converting...")
    #         input_path = os.path.join(input_folder, filename)
    #         output_path = os.path.join(output_folder, filename.replace('.xpt', '.csv'))
    #         convert_xpt_to_csv(input_path, output_path)
    #     else:
    #         print(f"File {filename} is not an XPT file, skipping.")

    # Process each XPT file in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.xpt'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.rsplit('.', 1)[0] + '.csv')
            convert_xpt_to_csv(input_path, output_path)
            # Ensure the data directory exists
            os.makedirs('data', exist_ok=True)
            # Define the output file
            output_file = os.path.join('data', 'nhanes_output.txt')
            # Append the results to the file
            append_to_file(output_file, f"File converted: {filename}\n")
        else:
            print(f"File {filename} is not an XPT file, skipping.")
            # Ensure the data directory exists
            os.makedirs('data', exist_ok=True)
            # Define the output file
            output_file = os.path.join('data', 'nhanes_output.txt')
            # Append the results to the file
            append_to_file(output_file, f"File not converted: {filename}\n")




# Main execution
if __name__ == "__main__":
    input_folder = r"C:\Source\CapstoneTwoHTNandParameters\NHANESPackageTest\NHANES\raw_data\2003-2004a"  # Replace with your input folder path
    output_folder = r"C:\Source\CapstoneTwoHTNandParameters\NHANESPackageTest\NHANES\raw_data\2003-2004a"  # Replace with your output folder path
    print(f"Files in input folder: {os.listdir(input_folder)}")
    process_folder(input_folder, output_folder)
    print("Conversion process completed.")



