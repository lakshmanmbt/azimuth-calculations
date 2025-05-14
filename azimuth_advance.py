import os
import pandas as pd
import math

# Load the Excel file
file_path = r'C:\Users\Administrator\Downloads\azimuth formula\Excel input\dummy1.xlsx'
df = pd.read_excel(file_path)

# Extract latitude and longitude columns
latitudes = df['latitude']
longitudes = df['longitude']

def calculate_azimuth(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Calculate the difference in longitude
    delta_lon = lon2 - lon1
    
    # Azimuth calculation
    x = math.sin(delta_lon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon)
    
    azimuth = math.atan2(x, y)
    
    # Convert from radians to degrees
    azimuth = math.degrees(azimuth)
    
    # Normalize the azimuth to 0° - 360°
    azimuth = (azimuth + 360) % 360
    
    return azimuth

# Calculate azimuths between consecutive points
azimuths = []
for i in range(len(latitudes) - 1):
    azimuth = calculate_azimuth(latitudes[i], longitudes[i], latitudes[i + 1], longitudes[i + 1])
    azimuths.append(azimuth)

# Add the azimuths to the DataFrame (you can choose how to handle the first point)
df['azimuth'] = pd.Series([None] + azimuths)  # First point has no azimuth

# Extract the file name from the input path
input_file_name = os.path.basename(file_path)

# Define the output folder path
output_folder = r'C:\Users\Administrator\Downloads\azimuth formula\Excel output'

# Create the full output file path using the input file name
output_file_path = os.path.join(output_folder, input_file_name)

# Save the DataFrame with azimuths to the new file in the output folder
df.to_excel(output_file_path, index=False)

print(f"Azimuths calculated and saved to {output_file_path}.")


