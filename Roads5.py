# Make sure you have ArcGIS Pro installed (the code worked on v3.0.3)
# Open Python Command Prompt
# Navigate to the following directory
# cd C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Roads\5
# Run the code
# python Roads5.py



import arcpy
import pandas as pd
import os

def estimate_length_in_km(length_in_degrees, latitude=49.25):
    # Approximate conversion for latitude
    km_per_degree = 111
    # Convert length
    length_in_km = length_in_degrees * km_per_degree
    return length_in_km

# Define the file paths
roads_shp = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Roads\2\Roads2.shp"
watershed_shp = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Raw_Data\Watersheds\1\OWBTERT\LIO-2023-01-26\ONT_WSHED_BDRY_TERT_DERIVED.shp"
output_folder = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Roads\5"
intersect_output = os.path.join(output_folder, "IntersectedRoads.shp")

# Allow overwrite of existing files
arcpy.env.overwriteOutput = True

# Intersect roads with watersheds
arcpy.Intersect_analysis([roads_shp, watershed_shp], intersect_output)

# Create a dictionary to store the estimated road lengths per watershed in km
results_km = {}

# Loop through each intersected road segment
with arcpy.da.SearchCursor(intersect_output, ["NAME", "ST_TYPE_S", "SHAPE@LENGTH"]) as cursor:
    for row in cursor:
        watershed_name = row[0]
        road_type = row[1]
        road_length_degrees = row[2]
        
        road_length_km = estimate_length_in_km(road_length_degrees)
        
        # Initialize nested dictionary if watershed not in results_km
        if watershed_name not in results_km:
            results_km[watershed_name] = {}
        
        # Sum up lengths based on road type
        if road_type not in results_km[watershed_name]:
            results_km[watershed_name][road_type] = 0
        results_km[watershed_name][road_type] += road_length_km

# Convert the results dictionary to a pandas DataFrame
df_km = pd.DataFrame(results_km).transpose()

# Save the DataFrame to an Excel file
output_excel_km = os.path.join(output_folder, "EstimatedRoadLengthsByWatershed_km.xlsx")
df_km.to_excel(output_excel_km)

