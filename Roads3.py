# Make sure you have ArcGIS Pro installed (the code worked on v3.0.3)
# Open Python Command Prompt
# Navigate to the following directory
# cd C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Roads\3
# Run the code
# python Roads3.py



import arcpy
import pandas as pd
import os

# Define the file paths
roads_shp = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Roads\2\Roads2.shp"
watershed_shp = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Raw_Data\Watersheds\1\OWBTERT\LIO-2023-01-26\ONT_WSHED_BDRY_TERT_DERIVED.shp"
output_folder = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Roads\3"

# Allow overwrite of existing files
arcpy.env.overwriteOutput = True

# Create feature layers for both roads and watersheds
roads_lyr = arcpy.MakeFeatureLayer_management(roads_shp, "roads_lyr")
watershed_lyr = arcpy.MakeFeatureLayer_management(watershed_shp, "watershed_lyr")

# Create a dictionary to store the road lengths per watershed
results = {}

# Loop through each watershed
with arcpy.da.SearchCursor(watershed_lyr, ["FID", "NAME"]) as cursor:
    for row in cursor:
        watershed_id = row[0]
        watershed_name = row[1]
        
        # Select the current watershed
        arcpy.SelectLayerByAttribute_management(watershed_lyr, "NEW_SELECTION", f"FID = {watershed_id}")
        
        # Select roads that intersect with the current watershed
        arcpy.SelectLayerByLocation_management(roads_lyr, "INTERSECT", watershed_lyr)
        
        # Loop through each selected road and sum up lengths based on their type
        road_lengths = {}
        with arcpy.da.SearchCursor(roads_lyr, ["ST_TYPE_S", "LENGTH"]) as road_cursor:
            for road_row in road_cursor:
                road_type = road_row[0]
                road_length = road_row[1]
                
                if road_type not in road_lengths:
                    road_lengths[road_type] = 0
                road_lengths[road_type] += road_length
        
        results[watershed_name] = road_lengths

# Convert the results dictionary to a pandas DataFrame
df = pd.DataFrame(results).transpose()

# Save the DataFrame to an Excel file
output_excel = os.path.join(output_folder, "RoadLengthsByWatershed.xlsx")
df.to_excel(output_excel)
