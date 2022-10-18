import math
import utm # Coordinates are converted to UTM format for analysis in metres (assume they are in same zone)

import sys
import copy

# Take a list of lat/lon coords and extract out the easting and northing vectors (in m)
# NOTE: For the purposes of this exercise we can ignore differing zone letters and numbers
def convert_to_utm_xy(coordinates):
    return [utm.from_latlon(*c)[:2] for c in coordinates]

def calc_total_distance(coordinates_xy, indices):
    total_distance = 0
    for i in range(1, len(indices)):
        dx = coordinates_xy[indices[i]][0] - coordinates_xy[indices[i-1]][0]
        dy = coordinates_xy[indices[i]][1] - coordinates_xy[indices[i-1]][1]
        total_distance += math.sqrt(dx*dx + dy*dy)
    return total_distance

def optimise_travel_order(coordinates):
    coordinates_xy = convert_to_utm_xy(coordinates)
    indices = list(range(len(coordinates_xy)))
    
    # TODO Devise an algorithm to optimise the order

    current_best = copy.copy(coordinates_xy)

    print(current_best)

    start_location = coordinates_xy.pop(0)
    current_order = []
    current_order.append(start_location)

    global current_best_distance
    set_current_best_distance(sys.maxsize)

    dfs(coordinates_xy, current_order, 0, start_location)

    # Testing the code optimisation
    print("Current best:")
    print(get_current_best())
    print(len(get_current_best()))
    print(calc_total_distance(get_current_best(),indices))
    
    return indices

def calc_distance(start, end):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    return math.sqrt(dx*dx + dy*dy)

def set_current_best_distance(new_distance):
    global current_best_distance 
    current_best_distance = new_distance

def get_current_best_distance():
    return current_best_distance

def set_current_best(new_best):
    global current_best
    current_best = new_best

def get_current_best():
    return current_best

def dfs(remaining_list, current_order, current_distance, prev_location):
    if len(remaining_list) <= 1:
        new_remaining_list = copy.copy(remaining_list)
        location = new_remaining_list.pop(0)
        new_current_distance = current_distance + calc_distance(prev_location, location)
        new_order = copy.copy(current_order)
        new_order.append(location)

        if(new_current_distance < get_current_best_distance()):
            set_current_best_distance(new_current_distance)
            current_best = copy.copy(new_order)
            set_current_best(current_best)

    else: 
        #Need to loop through for all potential 
        for x in range(len(remaining_list)):

            temp_list = copy.copy(remaining_list)

            temp_location = temp_list.pop(x)
            temp_order = copy.copy(current_order)
            temp_order.append(temp_location)
            temp_distance = current_distance + calc_distance(prev_location, temp_location)

            if temp_distance < get_current_best_distance():  
                dfs(temp_list, temp_order,temp_distance, temp_location)


# Testing the algorithm locally
coordinates = [
    (-36.932197, 174.987783),
    (-36.969210, 174.912630),
    (-37.008773, 174.835551),
    (-36.812159, 174.782783),
    (-36.987639, 174.850803),
    (-36.987525, 174.756794)
]

# coordinates = [
#     (-38.444208, 175.821467),
#     (-37.103197, 174.877639),
#     (-36.771995, 174.582458),
#     (-37.189848, 174.921181),
#     (-37.788692, 175.221970),
#     (-37.027575, 174.997799),
#     (-38.131145, 176.166297),
#     (-36.303898, 174.523462),
#     (-37.548307, 175.711875),
#     (-38.660265, 176.032597),
#     (-37.008849, 174.832011),
#     (-36.898576, 174.593211),
#     (-37.279678, 175.374855),
#     (-36.998122, 175.037219),
#     (-36.701624, 174.725347)
# ]

indices = optimise_travel_order(coordinates)
# coordinates_xy = convert_to_utm_xy(coordinates)
# total_distance = calc_total_distance(coordinates_xy, indices)

# print(total_distance)