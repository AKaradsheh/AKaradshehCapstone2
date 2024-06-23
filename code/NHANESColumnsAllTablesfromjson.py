import json
import csv
import os

# Load the JSON data
json_data = {
    "Age": ["RIDAGEYR"],
    "Gender": ["RIAGENDR"],
    "Survey": ["SDDSRVYR"],
    "Season of year": ["RIDEXMON"],
    "Ethnicity": ["RIDRETH3", "RIDRETH1"],
    "Poverty status": ["INDFMPIR"],
    "Education level": ["DMDEDUC2"],
    "Mortality event": ["MORTSTAT"],
    "Mortality tte": ["PERMTH_INT"],
    "Occupation hours worked": ["OCQ180"],
    "Occupation shift-work": ["OCQ265"],
    "Unemployment status": ["OCQ380"],
    "Occupation status": ["OCQ150", "OCD150"],
    "Weight (kg)": ["BMXWT"],
    "Height (cm)": ["BMXHT"],
    "BMI (kg/m2)": ["BMXBMI"],
    "Alcohol drinks days per year": ["ALQ120Q"],
    "Alcohol drinks num per time": ["ALQ130"],
    "Smoking status": ["SMQ020", "SMQ120", "SMQ150"],
    "Smoking regularly": ["SMD030", "SMD130", "SMD160"],
    "Smoking now": ["SMQ040", "SMQ140", "SMQ170"],
    "Health general": ["HSD010"],
    "Health physical poor (days)": ["HSQ470"],
    "Health mental poor (days)": ["HSQ480"],
    "Hospital/healthcare frequency last yr": ["HUQ050", "HUQ051"],
    "Hospitalization number last yr": ["HUD080", "HUQ080"],
    "Hospitalization last yr": ["HUD070", "HUQ070", "HUQ071"],
    "Depression Low interest": ["DPQ010"],
    "Depression Feel hopeless": ["DPQ020"],
    "Depression Trouble sleeping": ["DPQ030"],
    "Depression Feel tired": ["DPQ040"],
    "Depression Trouble appetite": ["DPQ050"],
    "Depression Feel bad": ["DPQ060"],
    "Depression Trouble concentrating": ["DPQ070"],
    "Depression Trouble speaking": ["DPQ080"],
    "Depression Feel better dead": ["DPQ090"],
    "Depression Caused difficulties": ["DPQ100"],
    "Physical activity vigorous": ["PAD200", "PAQ650"],
    "Physical activity moderate": ["PAD320", "PAQ665"],
    "Respiratory Cough most days": ["RDQ031", "RDQ030", "RDD030"],
    "Respiratory Bring up phlegm": ["RDQ050"],
    "Respiratory Wheezing in chest": ["RDQ070"],
    "Respiratory Limited activity": ["RDQ135"],
    "Respiratory Dry cough at night": ["RDQ140"],
    "Respiratory Shortness of breath": ["CDQ010"],
    "How often feel overly sleepy during day": ["SLQ120"],
    "Sleep hours (weekday)": ["SLD010H", "SLD012"],
    "Sleep hours (weekend)": ["SLD013"],
    "Sleep trouble": ["SLQ050"],
    "Sleep disorder": ["SLQ060"],
    "Hypertension": ["BPQ030"],
    "Diabetes": ["DIQ010"],
    "Asthma": ["MCQ010"],
    "Anemia": ["MCQ053"],
    "Psoriasis": ["MCQ070"],
    "Overweight": ["MCQ080"],
    "Hay fever": ["MCQ120A", "AGQ030"],
    "Cancer of any kind": ["MCQ220"],
    "Arthritis": ["MCQ160A"],
    "Congestive heart failure (CHF)": ["MCQ160B"],
    "Coronary heart disease (CHD)": ["MCQ160C"],
    "Angina pectoris": ["MCQ160D"],
    "Heart attack (MI)": ["MCQ160E"],
    "Stroke": ["MCQ160F"],
    "Emphysema": ["MCQ160G"],
    "Bronchitis": ["MCQ160K"],
    "Liver condition": ["MCQ160L"],
    "Thyroid condition": ["MCQ160M", "MCQ160I"],
    "Gout": ["MCQ160N"],
    "COPD": ["MCQ160O"],
    "Chronic lower respiratory diseases": ["MCQ160G", "MCQ160K", "MCQ160O"],
    "Osteoporosis": ["OSQ060"]
}

# Prepare data for CSV
csv_data = []
for key, values in json_data.items():
    row = [key] + values
    csv_data.append(row)

# Determine the maximum number of columns
max_columns = max(len(row) for row in csv_data)

# Create 'data' directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Write to CSV
csv_file_path = os.path.join('data', 'nhanes_variables.csv')
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write header
    header = ['Variable'] + [f'Code_{i + 1}' for i in range(max_columns - 1)]
    writer.writerow(header)

    # Write data
    for row in csv_data:
        # Pad rows with empty strings if they have fewer columns than the maximum
        padded_row = row + [''] * (max_columns - len(row))
        writer.writerow(padded_row)

print(f"CSV file has been created at: {csv_file_path}")


# ______________________________________________________________________________

# Function to append text to a file
def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text + '\n')


# Define the output file
output_file = os.path.join('data', 'nhanes_output.txt')

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

append_to_file(output_file, "\n")  # Add a blank line for separation

# Append to the file
append_to_file(output_file, f"File Names: {csv_file_path}\n")


# print to the console as well
print(f"appended : {csv_file_path}")
