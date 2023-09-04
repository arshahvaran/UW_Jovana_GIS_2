# Open Python Command Prompt
# Navigate to the following directory
# cd C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Roads\6
# Run the code
# python final.py



import pandas as pd

# Load the processed data from the "processed_data.xlsx" file
input_path = "C:\\Users\\PHYS3009\\Desktop\\Jovana_GIS_2\\Ontario\\Processed_Data\\Roads\\6\\processed_data.xlsx"
processed_df = pd.read_excel(input_path)

# Create the new DataFrame
output_df = pd.DataFrame()
output_df['Watershed'] = processed_df.iloc[:, 0]  # First column is the same
output_df['Sum'] = processed_df.iloc[:, 1:].sum(axis=1)  # Sum across rows

# Normalize the Sum values
min_val = output_df['Sum'].min()
max_val = output_df['Sum'].max()
output_df['Normalized'] = (output_df['Sum'] - min_val) / (max_val - min_val)

# Save the output to a new file named "summary_data.xlsx"
output_path_summary = "C:\\Users\\PHYS3009\\Desktop\\Jovana_GIS_2\\Ontario\\Processed_Data\\Roads\\6\\final.xlsx"
output_df.to_excel(output_path_summary, index=False)
