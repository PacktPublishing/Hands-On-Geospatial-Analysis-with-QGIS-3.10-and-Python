import pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt
import os
from shapely.geometry import Point


## Setting project root directory
os.chdir("/Users/jane/Documents/Caffeine/work/Packt/Q_Py/Section2/Data")

## Parks dataframe
parks = pd.read_csv("parks.csv")

## See the first 5 entries of the parks dataframe
print(parks.head())

## Print the parks object type
print(type(parks))

## Define geometry (fill in Longitude and Latitude in the right order)
geometry = [Point(xy) for xy in zip(parks['Longitude'], parks['Latitude'])]

# Assign coordinate reference system : WGS84
crs = {'init': 'epsg:4326'}

# Creating a geographic data frame
parks_gdf = gp.GeoDataFrame(parks, crs=crs, geometry=geometry)
print(parks_gdf.head())
parks_gdf.plot(marker='o', color='#3e3e3e', markersize=10)

# view the plot in a new window
plt.show()