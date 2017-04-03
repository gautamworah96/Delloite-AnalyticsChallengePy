
import csv

# Open the earthquake data file.
filename = 'location.csv'

# Create empty lists for the data we are interested in.
lats, lons = [], []
#magnitudes = []
#timestrings = []

# Read through the entire file, skip the first line,
#  and pull out just the lats and lons.
with open(filename) as f:
    # Create a csv reader object.
    reader = csv.reader(f)
    
    # Ignore the header row.
    next(reader)
    
    # Store the latitudes and longitudes in the appropriate lists.
    for row in reader:
        lats.append(float(row[0]))
        lons.append(float(row[1]))
        #magnitudes.append(float(row[4]))
        #timestrings.append(row[0])
        
# --- Build Map ---
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

'''def get_marker_color(magnitude):
    # Returns green for small earthquakes, yellow for moderate
    #  earthquakes, and red for significant earthquakes.
    if magnitude < 3.0:
        return ('go')
    elif magnitude < 5.0:
        return ('yo')
    else:
        return ('ro')'''
 
eq_map = Basemap(projection='robin', resolution = 'h', area_thresh = 1000.0,
              lat_0=0, lon_0=-130)
eq_map.drawcoastlines()
eq_map.drawcountries()
#eq_map.fillcontinents(color = 'gray')
eq_map.bluemarble()
eq_map.drawmapboundary()
eq_map.drawmeridians(np.arange(0, 360, 30))
eq_map.drawparallels(np.arange(-90, 90, 30))
 
min_marker_size = 2.25
for lon, lat in zip(lons, lats):
    x,y = eq_map(lon, lat)
    
    #marker_string = get_marker_color(mag)
    eq_map.plot(x, y,'ro', markersize=5)
    

plt.title('Location of all plane disappearances')


plt.figure(figsize=(16,12))
plt.show()

