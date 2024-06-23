

from nhanes.load import load_NHANES_data, load_NHANES_metadata

data_df = load_NHANES_data(year='2003-2004')
metadata_df = load_NHANES_metadata(year='2003-2004')

print(data_df.head())
print(metadata_df.head(100))