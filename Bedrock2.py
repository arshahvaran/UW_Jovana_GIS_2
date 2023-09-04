# Make sure you have ArcGIS Pro installed (the code worked on v3.0.3)
# Open Python Command Prompt
# Navigate to the following directory
# cd C:\Users\PHYS3009\Desktop\Jovana_GIS_2\Ontario\Processed_Data\Bedrock\2
# Run the code
# python Bedrock2.py



import arcpy
import pandas as pd

# Setup
arcpy.env.workspace = "C:\\Users\\PHYS3009\\Desktop\\Jovana_GIS_2\\Ontario\\Processed_Data\\Bedrock\\1"
arcpy.env.overwriteOutput = True

# Read the categories from the Excel file to create the mapping dictionary
xls_path = "C:\\Users\\PHYS3009\\Desktop\\Jovana_GIS_2\\Ontario\\Processed_Data\\Bedrock\\2\\Categories.xlsx"
xls = pd.ExcelFile(xls_path)
sheet_names = xls.sheet_names

sheets_data = {}
for sheet in sheet_names:
    sheets_data[sheet] = pd.read_excel(xls, sheet)

# Create a dictionary mapping OID_ to the category
oid_to_category = {}
for category, data in sheets_data.items():
    for oid in data['OID_']:
        oid_to_category[oid] = category

# Input & Output
input_shapefile = "Bedrock.shp"
output_directory = "C:\\Users\\PHYS3009\\Desktop\\Jovana_GIS_2\\Ontario\\Processed_Data\\Bedrock\\2"
output_shapefile = "Bedrock2.shp"

# Create a new shapefile with the same structure as the original
arcpy.CreateFeatureclass_management(output_directory, output_shapefile, template=input_shapefile)

# Loop through the records of the original shapefile and group them into categories
with arcpy.da.SearchCursor(input_shapefile, ["FID", "SHAPE@", "ROCKTYPE_P"]) as in_cursor:
    with arcpy.da.InsertCursor(output_shapefile, ["SHAPE@", "ROCKTYPE_P"]) as out_cursor:
        for row in in_cursor:
            oid = row[0]
            shape = row[1]
            category = oid_to_category.get(oid, None)
            if category:
                out_cursor.insertRow([shape, category])

print("Shapefile processed successfully!")

