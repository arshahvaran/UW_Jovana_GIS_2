# Make sure you have ArcGIS Pro installed (the code worked on v3.0.3)
# Open Python Command Prompt
# Navigate to the following directory
# cd C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Bedrock\5
# Run the code
# python Bedrock5.py



import arcpy

# Setup
arcpy.env.workspace = "C:\\Users\\PHYS3009\\Desktop\\Jovana_GIS_2\\Ontario\\Processed_Data\\Bedrock\\4"
arcpy.env.overwriteOutput = True

# Input & Output
input_shapefile = "Bedrock4.shp"
output_directory = "C:\\Users\\PHYS3009\\Desktop\\Jovana_GIS_2\\Ontario\\Processed_Data\\Bedrock\\5"
output_shapefile = "Bedrock5.shp"

# Dissolve polygons based on the ROCKTYPE_P attribute
arcpy.Dissolve_management(
    in_features=input_shapefile,
    out_feature_class=output_directory + "\\" + output_shapefile,
    dissolve_field="ROCKTYPE_P",
    statistics_fields="",  # No statistics fields
    multi_part="MULTI_PART",
    unsplit_lines="DISSOLVE_LINES"
)

print("Shapefile processed successfully!")
