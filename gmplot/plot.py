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
        rads = math.radians(bearing-270)
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

    return (b_lat,b_lon)

lat = 39.0833
lon = -76.5755

p = bearingLine(lat,lon,278.4)

lat_list = [lat,p[0]]
lon_list = [lon,p[1]]

gmap1 = gmplot.GoogleMapPlotter(39.0833,-76.5755,17)
gmap1.apikey = 'AIzaSyBKGW68OEyogCQxQTLqoaPKXxmBpV4kLkA'

gmap1.marker(lat,lon)
gmap1.plot(lat_list,lon_list)

gmap1.draw('map.html')
