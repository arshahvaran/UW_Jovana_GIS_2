# Make sure you have ArcGIS Pro installed (the code worked on v3.0.3)
# Open Python Command Prompt
# Navigate to the following directory
# cd C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\4
# Run the code
# python Misc4.py



import arcpy

# Set overwrite to true
arcpy.env.overwriteOutput = True

# Define the input shapefiles
hydroLakes_shp = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\4\Input\HydroLAKES_polys_v10_shp_Can.shp"
within_shp = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\4\Input\Anoxia_Within.shp"

# Define the output directory and shapefiles
output_dir = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\4\Output"
Lakes_W_A_shp = f"{output_dir}\\Lakes_W_A.shp"
Lakes_WO_A_shp = f"{output_dir}\\Lakes_WO_A.shp"

# Create a feature layer from HydroLAKES shapefile
arcpy.management.MakeFeatureLayer(hydroLakes_shp, "hydroLakes_lyr")

# Step 1: Select lakes with chloride measurements (Lakes_W_A)
arcpy.SelectLayerByLocation_management("hydroLakes_lyr", "INTERSECT", within_shp)
arcpy.management.CopyFeatures("hydroLakes_lyr", Lakes_W_A_shp)

# Step 2: Invert the selection to get lakes without chloride measurements (Lakes_WO_A)
arcpy.management.SelectLayerByAttribute("hydroLakes_lyr", "SWITCH_SELECTION")
arcpy.management.CopyFeatures("hydroLakes_lyr", Lakes_WO_A_shp)


