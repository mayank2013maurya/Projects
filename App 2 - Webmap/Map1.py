import folium
import pandas

data = pandas.read_csv("Volcanoes.csv")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"

    elif 1000 <= elevation < 3000:
        return "orange"

    else:
        return "red"

html = """
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
<style>
    a {
        font-family: Roboto, serif;
        color: red;
    }
    a:hover {
        color: black;
    }
    h4 {
        font-family: Roboto, serif;
    }
    p {
        font-family: Roboto, serif;
    }
</style>
<h4>Volcano name:</h4>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br/>
<p>Height: %s m</p>
"""

map = folium.Map(location=[37.0902, -95.7129], zoom_start = 6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el, nam in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html = html % (nam, nam, el), width = 200, height = 100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
    radius = 6, popup = folium.Popup(iframe), fill_color = color_producer(el), color = "grey",
    fill = True, fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data = open("world.json", "r", encoding = "utf-8-sig").read(),
 style_function = lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000
 else "purple" if 10000000 <= x["properties"]["POP2005"] < 20000000
 else "yellow" if 20000000 <= x["properties"]["POP2005"] < 100000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
