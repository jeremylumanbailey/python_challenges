# Import the necessary libraries
import pandas as pd
import gmplot
# For improved table display in the notebook
from IPython.display import display

raw_data = pd.read_csv("costarlocations.csv")

# Success! Display the first 5 rows of the dataset
display(raw_data.head(n=5))
display(raw_data.info())

# Let's limit the dataset to the first 15,000 records for this example
data = raw_data.head(n=15000)

# Store our latitude and longitude
latitudes = data["LAT"]
longitudes = data["LON"]

# Creating the location we would like to initialize the focus on.
# Parameters: Lattitude, Longitude, Zoom
gmap = gmplot.GoogleMapPlotter(34.0522, -118.2437, 10)

# Overlay our datapoints onto the map
gmap.heatmap(latitudes, longitudes)

# Generate the heatmap into an HTML file
gmap.draw("costarheatmap.html")
import pandas as pd
from opencage.geocoder import OpenCageGeocode
from geotext import GeoText
# import geograpy
f = open("textfile.txt", "r").read()
places = GeoText(f)
# places = GeoText("London is a great city")

list_cities = places.cities
list_cities = list(dict.fromkeys(list_cities))

print(list_cities)

# dfObj = pd.DataFrame(list_cities)
#
# print(dfObj.head())
# dfObj.to_csv("testdataframe.csv", index=False)


key = # https://opencagedata.com/ ""
#
geocoder = OpenCageGeocode(key)


list_lat = []

list_long = []

for x in range(len(list_cities)):
    query = str(list_cities[x])
    results = geocoder.geocode(query)
    lat = results[0]['geometry']['lat']
    long = results[0]['geometry']['lng']

    list_lat.append(lat)
    list_long.append(long)


dfObj1 = pd.DataFrame(list_lat)
dfObj2 = pd.DataFrame(list_long)

dfObj1.to_csv("lats.csv")
dfObj2.to_csv("longs.csv")


