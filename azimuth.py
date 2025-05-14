import math

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

# Example: Calculate azimuth between two points
lat1, lon1 = 34.0522, -118.2437  # Los Angeles (in degrees)
lat2, lon2 = 40.7128, -74.0060   # New York City (in degrees)
azimuth = calculate_azimuth(lat1, lon1, lat2, lon2)
print(f"Azimuth (bearing) from Los Angeles to New York City: {azimuth:.2f}°")
