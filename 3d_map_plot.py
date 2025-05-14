import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load the Excel file
file_path = r'C:\Users\Administrator\Downloads\azimuth formula\Excel input\dummy1.xlsx'
df = pd.read_excel(file_path)

# Extract latitude and longitude columns
latitudes = df['latitude']
longitudes = df['longitude']

# Create a figure with the Orthographic (3D globe-like) projection
fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection=ccrs.Orthographic(central_longitude=77, central_latitude=12))  # Center the globe around your data

# Add features like coastlines, borders, and land
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)

# Plot the latitude and longitude points on the globe
ax.scatter(longitudes, latitudes, color='red', s=20, transform=ccrs.PlateCarree())

# Set title and show the plot
plt.title("3D Globe with Lat/Long Data", fontsize=15)
plt.show()
