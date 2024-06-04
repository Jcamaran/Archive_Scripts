import os
import pandas as pd

# Define paths
input_folder = r"PATH_to_input_folder"
output_folder = r"PATH_to_output_folder"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    if filename.endswith(".xlsx"):
        try:
            # Read the Excel file with openpyxl engine
            df = pd.read_excel(file_path, engine='openpyxl')
            # Define the CSV file path
            csv_filename = os.path.splitext(filename)[0] + ".csv"
            csv_file_path = os.path.join(output_folder, csv_filename)
            # Save the dataframe as a CSV file
            df.to_csv(csv_file_path, index=False)
            print(f"Converted {filename} to {csv_filename}")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")
    elif filename.endswith(".xls"):
        try:
            # Read the Excel file with xlrd engine
            df = pd.read_excel(file_path, engine='xlrd')
            # Define the CSV file path
            csv_filename = os.path.splitext(filename)[0] + ".csv"
            csv_file_path = os.path.join(output_folder, csv_filename)
            # Save the dataframe as a CSV file
            df.to_csv(csv_file_path, index=False)
            print(f"Converted {filename} to {csv_filename}")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")
    else:
        print(f"Skipped non-Excel file: {filename}")
