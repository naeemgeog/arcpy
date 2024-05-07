#-----By Naeem----convert too many excel file data into One CSv file and give the name 2000_1 to 2021_12 all column headings name 
#---if you want to convert too many Excell files data into one csv file 
# -------This use for 1 km pte mean excel files into one csv  
# Excel files to in one csv files 
import pandas as pd
import os

# Define input and output file paths
input_folder = r'E:\Data_Arcpy\Exceloutput'
output_file = r'E:\Data_Arcpy\Excel1file\PET.csv'

# Function to read and process input files
def process_input_files(input_folder):
    all_data = []
    for filename in os.listdir(input_folder):
        if filename.endswith(".xls"):  # Assuming all input files are in .xls format
            file_path = os.path.join(input_folder, filename)
            data = pd.read_excel(file_path)
            if 'MEAN' in data.columns:
                year_month = filename.split("_")
                if len(year_month) == 2:
                    year = int(year_month[0])
                    month = int(year_month[1].split(".")[0])
                    data = data.rename(columns={'MEAN': f'{year}_{month}'})
                    all_data.append(data[f'{year}_{month}'])
                else:
                    print(f"Warning: Unexpected filename format '{filename}'. Skipping...")
            else:
                print(f"Warning: 'MEAN' column not found in file '{filename}'. Skipping...")
    return pd.concat(all_data, axis=1)

# Main function
def main():
    combined_data = process_input_files(input_folder)
    combined_data.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()

