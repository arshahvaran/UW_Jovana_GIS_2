# Open Python Command Prompt
# Navigate to the following directory
# cd C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Roads\6
# Run the code
# python Roads6.py



import pandas as pd

# Load the coefficients from the "kgperkm.xlsx" file
coefficients_path = "C:\\Users\\PHYS3009\\Desktop\\Jovana_GIS_2\\Ontario\\Processed_Data\\Roads\\6\\kgperkm.xlsx"
coefficients_df = pd.read_excel(coefficients_path)
coefficients_dict = coefficients_df.set_index('ST_TYPE_S2')['kgkmC'].to_dict()

# Load the data from the "data.xlsx" file
data_path = "C:\\Users\\PHYS3009\\Desktop\\Jovana_GIS_2\\Ontario\\Processed_Data\\Roads\\6\\data.xlsx"
data_df = pd.read_excel(data_path)

# Multiply each column by its corresponding coefficient
for column in data_df.columns[1:]:
    data_df[column] = data_df[column] * coefficients_dict[column]

# Save the modified data to a new file named "processed_data.xlsx"
output_path = "C:\\Users\\PHYS3009\\Desktop\\Jovana_GIS_2\\Ontario\\Processed_Data\\Roads\\6\\processed_data.xlsx"
data_df.to_excel(output_path, index=False)

