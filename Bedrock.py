# Make sure you have ArcGIS Pro installed (the code worked on v3.0.3)
# Open Python Command Prompt
# Navigate to the following directory
# cd C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Bedrock\1
# Run the code
# python Bedrock.py



import arcpy

# Set workspace and allow overwrite
arcpy.env.workspace = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Raw_Data\Bedrock\MRD126-REV1\MRD126-REVISION1\MRD126-REV1\ShapeFiles\Geology"
arcpy.env.overwriteOutput = True

# Define input and output paths
input_shapefile = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Raw_Data\Bedrock\MRD126-REV1\MRD126-REVISION1\MRD126-REV1\ShapeFiles\Geology\Geopoly.shp"
output_shapefile = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Bedrock\1\Bedrock.shp"

# Dissolve based on the "ROCKTYPE_P" attribute
arcpy.Dissolve_management(in_features=input_shapefile, 
                          out_feature_class=output_shapefile, 
                          dissolve_field="ROCKTYPE_P", 
                          multi_part="MULTI_PART", 
                          unsplit_lines="DISSOLVE_LINES")

print("Dissolve completed successfully!")

