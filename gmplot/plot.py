import gmplot
import math

def bearingLine(lat,lon,bearing,d=.05):
    if bearing == 0:
        b_lat = lat + d
        b_lon = lon

    elif bearing == 90:
        b_lat = lat
        b_lon = lon + d

    elif bearing == 180:
        b_lat = lat - d
        b_lon = lon

    elif bearing == 270:
        b_lat = lat
        b_lon = lon - d

    elif bearing > 0 and bearing < 90:
        rads = math.radians(bearing)
        tan = math.tan(rads)

        adj = math.sqrt((d**2)/(1+tan**2))
        b_lat = lat + adj

        opp = math.sqrt((tan**2*d**2)/(1+tan**2))
        b_lon = lon + opp

    elif bearing > 90 and bearing < 180:
        rads = math.radians(180-bearing)
        tan = math.tan(rads)

        adj = math.sqrt((d**2)/(1+tan**2))
        b_lat = lat - adj

        opp = math.sqrt((tan**2*d**2)/(1+tan**2))
        b_lon = lon + opp

    elif bearing > 180 and bearing < 270:
        rads = math.radians(bearing-180)
        tan = math.tan(rads)

        adj = math.sqrt((d**2)/(1+tan**2))
        b_lat = lat - adj

        opp = math.sqrt((tan**2*d**2)/(1+tan**2))
        b_lon = lon - opp

    elif bearing > 270 and bearing < 360:
        rads = math.radians(360-bearing)
        tan = math.tan(rads)

        adj = math.sqrt((d**2)/(1+tan**2))
        b_lat = lat + adj

        opp = math.sqrt((tan**2*d**2)/(1+tan**2))
        b_lon = lon - opp

    lat_list = [lat,b_lat]
    lon_list = [lon,b_lon]

    gmap1.marker(lat,lon,'cornflowerblue')
    gmap1.plot(lat_list,lon_list,'cornflowerblue',edge_width=3)

    return

#Tells Google Map where to
gmap1 = gmplot.GoogleMapPlotter(38.9837275,-76.4855159,18)
gmap1.apikey = 'AIzaSyBKGW68OEyogCQxQTLqoaPKXxmBpV4kLkA'

bearingLine(38.983400,-76.484368,280)
bearingLine(38.984117,-76.485747,185)
bearingLine(38.983025,-76.486616,54)

gmap1.draw('map.html')
