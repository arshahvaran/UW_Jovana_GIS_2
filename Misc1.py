# Make sure you have ArcGIS Pro installed (the code worked on v3.0.3)
# Open Python Command Prompt
# Navigate to the following directory
# cd C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\1
# Run the code
# python Misc1.py



import arcpy

# Enable overwriting output
arcpy.env.overwriteOutput = True

# Define the shapefile paths
chloride_shp = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\1\Chloride3\Chloride3.shp"
hydro_lakes_shp = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\1\HydroLAKES_polys_v10_shp_Can\HydroLAKES_polys_v10_shp_Can.shp"
output_dir = r"C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Miscellaneous\1\Output"

# Spatial Join output shapefile
join_output_shp = output_dir + "\\Within.shp"

# Chloride points that are outside lakes
not_within_output_shp = output_dir + "\\Outside.shp"

# Perform the Spatial Join
arcpy.analysis.SpatialJoin(chloride_shp, hydro_lakes_shp, join_output_shp, join_type="KEEP_COMMON", match_option="WITHIN")

# Create a new layer from the chloride shapefile
arcpy.management.MakeFeatureLayer(chloride_shp, "chloride_lyr")

# Select the features in the new layer that are identical to those in the joined shapefile
arcpy.management.SelectLayerByLocation("chloride_lyr", "ARE_IDENTICAL_TO", join_output_shp)

# Invert the selection to get points that are outside lakes
arcpy.management.SelectLayerByAttribute("chloride_lyr", "SWITCH_SELECTION")

# Write the selected features to a new shapefile
arcpy.management.CopyFeatures("chloride_lyr", not_within_output_shp)

# Export to Excel
# For joined points
arcpy.conversion.TableToExcel(join_output_shp, output_dir + "\\Within.xlsx")

# For points outside any lakes
arcpy.conversion.TableToExcel(not_within_output_shp, output_dir + "\\Outside.xlsx")
