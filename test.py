'''
Module Summary:
 -Test this works!
Inputs:
 -
Outputs:
 -
Author:
 - Olivia Whitehead : olivia.whitehead@baesystems.com
Team:
 -
Date:
- 10/11/2020     
 '''
import math
import random
import geopy
import geopy.distance
from geopy.distance import geodesic

def inputdata():
    '''
    Summary:
    -Get data from Kafka producer
    Inputs:
    -
    Returns:
    -
    '''
    return None

def numgenerator():
    '''
    Summary:
     -Generate random latitude and longitudes
    '''
    latitude = random.randrange(90) 
    longitude = random.randrange(180)
    lat = []
    lon = []
    for x in range(100):
        latitude+=0.3
        longitude+=0.7
        lat.append(latitude)
        lon.append(longitude)
    #print("latitude;", lat, '\n\r')   
    #print("longitude;", lon, '\n\r') 
    return lat, lon

def print_nicely(my_dict):
    '''
    Summary:
            - Print things out nicely
    '''

    for entry in my_dict:
        # NB: Sometimes data contains None for lat/long, make sure to check
        if (my_dict[entry]['lat'] is not None) and (my_dict[entry]['lon'] is not None):
            print("New Entry: %s | Latitude %.3f | Longitude %.3f" % (entry, my_dict[entry]['lat'], my_dict[entry]['lon']))

    return None

def TargetDistance(my_dict):
    '''
    Summary:
        -Finds the target distance between each plane and Frimley office (51.315432, -0.745697)
    Inputs:
        -Dictionary from ADSB data
    Outputs:
        -Distance
    '''
    MyDistances = {}
    OurPosition = (51.315432, -0.745697)
    for entry in my_dict:
        # NB: Sometimes data contains None for lat/long, make sure to check
        if (my_dict[entry]['lat'] is not None) and (my_dict[entry]['lon'] is not None):
            distance = geodesic(OurPosition, (my_dict[entry]['lat'], my_dict[entry]['lon'])).miles
            MyDistances[entry] = distance
            print("Flight %s | Distance: %.4f" % (entry,distance))
    return None



def CPA(lat, lon):
    '''
    Summary:
     -To calculate CPA between our position (London) and plane, need to caculate the distance between the start and end positions of the plane. 
     Will need to convert degrees to kilometers
    '''
    FlightPosition = []
    OurPosition = (51.5, 0.13)
    for i,j in zip(lat, lon):
        distance = geodesic(OurPosition, (i,j)).miles
        FlightPosition.append(distance)
    #print(FlightPosition)
    CPA = min(FlightPosition)
    print(CPA)

    return None

#lat, lon = numgenerator()
#CPA(lat, lon)
    


