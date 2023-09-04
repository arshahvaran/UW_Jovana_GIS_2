# Make sure you have ArcGIS Pro installed (the code worked on v3.0.3)
# Open Python Command Prompt
# Navigate to the following directory
# cd C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Roads\4
# Run the code
# python Roads4.py



import arcpy
import pandas as pd
import os

# Define the file paths
roads_shp = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Roads\2\Roads2.shp"
watershed_shp = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Raw_Data\Watersheds\1\OWBTERT\LIO-2023-01-26\ONT_WSHED_BDRY_TERT_DERIVED.shp"
output_folder = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Roads\4"
intersect_output = os.path.join(output_folder, "IntersectedRoads.shp")

# Allow overwrite of existing files
arcpy.env.overwriteOutput = True

# Intersect roads with watersheds
arcpy.Intersect_analysis([roads_shp, watershed_shp], intersect_output)

# Create a dictionary to store the road lengths per watershed
results = {}

# Loop through each intersected road segment
with arcpy.da.SearchCursor(intersect_output, ["NAME", "ST_TYPE_S", "SHAPE@LENGTH"]) as cursor:
    for row in cursor:
        watershed_name = row[0]
        road_type = row[1]
        road_length = row[2] / 1000  # Convert to kilometers
        
        # Initialize nested dictionary if watershed not in results
        if watershed_name not in results:
            results[watershed_name] = {}
        
        # Sum up lengths based on road type
        if road_type not in results[watershed_name]:
            results[watershed_name][road_type] = 0
        results[watershed_name][road_type] += road_length

# Convert the results dictionary to a pandas DataFrame
df = pd.DataFrame(results).transpose()

# Save the DataFrame to an Excel file
output_excel = os.path.join(output_folder, "RoadLengthsByWatershed.xlsx")
df.to_excel(output_excel)
