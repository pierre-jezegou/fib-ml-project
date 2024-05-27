"""This module contains functions to calculate the distance between two points"""
import math

PARIS = {
    'latitude': 48.866667,
    'longitude': 2.333333
}

def gps_coordinates_to_distance(latitude1:float,
             longitude1: float,
             latitude2: float,
             longitude2: float) -> float:
    '''Compute distance between two points in kilometers'''

    # Earth radius in meters
    earth_radius = 6371e3

    # Convert coordinates from degrees to radians
    latitude1_radians = latitude1 * math.pi/180
    latitude2_radians = latitude2 * math.pi/180
    delta_latitude_radians = (latitude2 - latitude1) * math.pi/180
    delta_longitude_radians = (longitude2 - longitude1) * math.pi/180

    # Calculate coefficients
    a = math.sin(delta_latitude_radians/2) * math.sin(delta_latitude_radians/2) + \
        math.cos(latitude1_radians) * math.cos(latitude2_radians) * \
        math.sin(delta_longitude_radians/2) * math.sin(delta_longitude_radians/2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    # Calculate distance in kilometers
    return (earth_radius * c)/1000

def distance_to_paris(latitude:float,
                      longitude: float
                      ) -> float:
    '''Compute distance between a point and Paris'''
    return gps_coordinates_to_distance(latitude, longitude, PARIS['latitude'], PARIS['longitude'])

rouen = [49.433331, 1.08333]
marseille = [43.296398, 5.370018]