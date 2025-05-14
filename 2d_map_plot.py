import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = r'C:\Users\Administrator\Downloads\azimuth formula\Excel input\dummy1.xlsx'
df = pd.read_excel(file_path)

# Display the first few rows of the dataframe to understand the data
print(df.head())

# Plotting 'longitude' vs 'latitude'
x_column = 'longitude'
y_column = 'latitude'

# Plotting the data
plt.plot(df[x_column], df[y_column], marker='o', linestyle='-', color='b')

# Adding labels and title
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title(f'{x_column} vs {y_column}')

# Show the plot
plt.show()
