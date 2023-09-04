# Open Python Command Prompt
# Navigate to the following directory
# cd C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Chloride\3
# Run the code
# python Chloride3.py



import pandas as pd

def dms_to_decimal(dms):
    """Convert DMS (Degrees, Minutes, Seconds) format to decimal degrees."""
    if pd.isnull(dms):
        return None
    dms = int(dms)
    degrees, remainder = divmod(dms, 10000)
    minutes, seconds = divmod(remainder, 100)
    return degrees + (minutes/60.0) + (seconds/3600.0)

# Load the data
df = pd.read_csv(r'C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Chloride\3\LPP_Chloride_2021.csv')

# Convert DMS coordinates to decimal degrees
df['Latitude (Decimal)'] = df['Latitude (DMS)'].apply(dms_to_decimal)
df['Longitude (Decimal)'] = df['Longitude (DMS)'].apply(dms_to_decimal)

# Make the longitude values negative for Western Hemisphere
df['Longitude (Decimal)'] = df['Longitude (Decimal)'].apply(lambda x: -abs(x) if pd.notnull(x) else x)

# Extract the year from the 'Date (DD-MMM-YY)' column
df['Year'] = pd.to_datetime(df['Date (DD-MMM-YY)']).dt.year

# Sort the dataframe by date and then drop duplicates based on Latitude and Longitude, keeping the last (latest) record
df = df.sort_values('Date (DD-MMM-YY)').drop_duplicates(subset=['Latitude (Decimal)', 'Longitude (Decimal)'], keep='last')

# Filter the dataframe to only keep rows with the highest "Chloride (mg/L)" value for each unique "Lake Name"
df = df.loc[df.groupby('Lake Name')['Chloride (mg/L)'].idxmax()]


# Normalize the chloride values
chloride_min = df['Chloride (mg/L)'].min()
chloride_max = df['Chloride (mg/L)'].max()
df['Chloride_Normalized'] = df['Chloride (mg/L)'].apply(lambda x: (x - chloride_min) / (chloride_max - chloride_min))

# Save the results to a CSV file
df.to_csv('Chloride3.csv', index=False)
