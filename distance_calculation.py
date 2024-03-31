import math


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


def how_many_are_near(latitude:float,
                      longitude: float,
                      monuments_coordinates: list[list[float]],
                      max_distance: float
                      ) -> int:
    '''Compute how many monuments are located near the target point'''
    counter = 0
    for monument in monuments_coordinates:
        if len(monument)!=2:
            continue
        computed_distance = gps_coordinates_to_distance(latitude,
                                                        longitude,
                                                        monument[0],
                                                        monument[1])
        if computed_distance <= max_distance:
            counter += 1

    return counter


paris = [48.866667, 2.333333]
rouen = [49.433331, 1.08333]

# print(gps_coordinates_to_distance(paris[0], paris[1], rouen[0], rouen[1]))
# print(how_many_are_near(paris[0], paris[1], [[48, 1]], 1000))
