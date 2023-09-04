# Make sure you have ArcGIS Pro installed (the code worked on v3.0.3)
# Open Python Command Prompt
# Navigate to the following directory
# cd C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Roads\4
# Run the code
# python unit.py



import arcpy
import pandas as pd
import os

# Define the file paths
roads_shp = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Roads\2\Roads2.shp"
desc = arcpy.Describe(roads_shp)
unit = desc.spatialReference.linearUnitName
print(unit)