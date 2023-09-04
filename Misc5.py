# Make sure you have ArcGIS Pro installed (the code worked on v3.0.3)
# Open Python Command Prompt
# Navigate to the following directory
# cd C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\5
# Run the code
# python Misc5.py



import arcpy

# Set environment settings
arcpy.env.overwriteOutput = True

# Paths to the shapefiles
shapefile1_path = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\5\Input\Lakes_W_A.shp"
shapefile2_path = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\5\Input\Lakes_W_Cl.shp"

# Output directory and shapefile name
output_dir = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\5\Output"
output_shapefile = "AandCl.shp"
output_path = f"{output_dir}\\{output_shapefile}"

# Get the spatial reference of the first shapefile
spatial_ref = arcpy.Describe(shapefile1_path).spatialReference

# Initialize lists to hold "Hylak_id" from both shapefiles
Hylak_ids_1 = []
Hylak_ids_2 = []

# Read "Hylak_id" from the first shapefile
with arcpy.da.SearchCursor(shapefile1_path, ["Hylak_id"]) as cursor:
    for row in cursor:
        Hylak_ids_1.append(row[0])

# Read "Hylak_id" from the second shapefile
with arcpy.da.SearchCursor(shapefile2_path, ["Hylak_id"]) as cursor:
    for row in cursor:
        Hylak_ids_2.append(row[0])

# Find common "Hylak_id" in both shapefiles
common_Hylak_ids = set(Hylak_ids_1).intersection(Hylak_ids_2)

# Create a new shapefile to store common features with the same spatial reference as the first shapefile
arcpy.CreateFeatureclass_management(output_dir, output_shapefile, "POLYGON", shapefile1_path, spatial_reference=spatial_ref)

# Copy features with common "Hylak_id" from first shapefile to output shapefile
with arcpy.da.SearchCursor(shapefile1_path, ["Hylak_id", "SHAPE@"]) as cursor:
    with arcpy.da.InsertCursor(output_path, ["Hylak_id", "SHAPE@"]) as icursor:
        for row in cursor:
            if row[0] in common_Hylak_ids:
                icursor.insertRow(row)

# Copy features with common "Hylak_id" from second shapefile to output shapefile
with arcpy.da.SearchCursor(shapefile2_path, ["Hylak_id", "SHAPE@"]) as cursor:
    with arcpy.da.InsertCursor(output_path, ["Hylak_id", "SHAPE@"]) as icursor:
        for row in cursor:
            if row[0] in common_Hylak_ids:
                icursor.insertRow(row)


