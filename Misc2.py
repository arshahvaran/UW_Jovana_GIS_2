# Make sure you have ArcGIS Pro installed (the code worked on v3.0.3)
# Open Python Command Prompt
# Navigate to the following directory
# cd C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\2
# Run the code
# python Misc2.py



import arcpy

# Set overwrite to true
arcpy.env.overwriteOutput = True

# Define the input shapefiles
hydroLakes_shp = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\2\Input\HydroLAKES_polys_v10_shp_Can.shp"
within_shp = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\2\Input\Within.shp"

# Define the output directory and shapefiles
output_dir = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\2\Output"
lakes_w_cl_shp = f"{output_dir}\\Lakes_W_Cl.shp"
lakes_wo_cl_shp = f"{output_dir}\\Lakes_WO_Cl.shp"

# Create a feature layer from HydroLAKES shapefile
arcpy.management.MakeFeatureLayer(hydroLakes_shp, "hydroLakes_lyr")

# Step 1: Select lakes with chloride measurements (Lakes_W_Cl)
arcpy.SelectLayerByLocation_management("hydroLakes_lyr", "INTERSECT", within_shp)
arcpy.management.CopyFeatures("hydroLakes_lyr", lakes_w_cl_shp)

# Step 2: Invert the selection to get lakes without chloride measurements (Lakes_WO_Cl)
arcpy.management.SelectLayerByAttribute("hydroLakes_lyr", "SWITCH_SELECTION")
arcpy.management.CopyFeatures("hydroLakes_lyr", lakes_wo_cl_shp)


