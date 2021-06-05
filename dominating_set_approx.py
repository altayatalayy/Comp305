__doc__ = '''Comp 305 final project
Group No: 21
Members:
    Altay Atalay
    Andrew Bond

Project Name: Pokemon
'''


def check_correctness(selected_cities, road_network):
    # check if the solution satisfies the problem
    has_center = {k: False for k in road_network.keys()}
    near_center = dict(has_center)

    # Mark cities with centers
    for city_name in selected_cities:
        has_center[city_name] = True  # if there is pokecenter

    # if any of the adjacent cities has center mark this city as near center
    for k in road_network.keys():
        for adj_city in road_network[k]:
            if has_center[adj_city]:
                near_center[k] = True

    # print(f'{has_center}, {near_center}')
    rv = all([h or n for h, n in zip(has_center.values(), near_center.values())])
    return rv


def network_from_file(file_name: str) -> dict:
    '''Create road network from input file
    '''
    keys: list = []  # Cities
    values: '2d list' = []  # Connected Cities 2d list

    with open(file_name) as f:
        for line in f.readlines():
            if line[0] == "#":  # Pass comments
                continue
            if line.strip() in ["", "\n"]:  # Pass empty lines
                continue
            l = line.split(' ')
            city_name, x, y, *connected_cities = l
            x, y = int(x[1]), int(y[0])  # Convert x and y from str to int
            connected_cities = [c.strip(',').strip('\n') for c in connected_cities]  # Get rid of the ,

            keys.append(city_name)
            values.append(connected_cities)

    road_network: dict = {k: v for k, v in zip(keys, values)}  # Create the road network usin keys and values
    return road_network


def findLargestVertex(road_network: dict, cities_list: list) -> str:
    if len(cities_list) == 0:
        return

    largestVertex = cities_list[0]
    numEdges = len(road_network[largestVertex])
    for i in range(1, len(cities_list)):
        length = len(road_network[cities_list[i]])
        if length > numEdges:
            largestVertex = cities_list[i]
            numEdges = len(road_network[cities_list[i]])

    return largestVertex

def helper(road_network : dict, cities_list: list):
    centersList = []
    while len(cities_list) > 0:
        largestVertex = findLargestVertex(road_network, cities_list)
        centersList.append(largestVertex)
        cities_list.remove(largestVertex)
        adjacent_cities = road_network[largestVertex]
        for city in adjacent_cities:
            if cities_list.__contains__(city):
                cities_list.remove(city)
    return centersList



def can_be_made_tournament_ready(road_network: dict, num_cities: int) -> list:
    '''The Algorithm
    '''
    if type(num_cities) not in [int, float] or num_cities < 0:
        raise ValueError(f'num cities must be a positive int')

    rv: list = []  # return value, list of cities

    if num_cities == 0:
        return rv

    centersList = helper(road_network, list(road_network.keys()))
    if len(centersList) <= num_cities:
        print("The approximation algorithm found a solution that satisfies the number of cities constraint.")

    return centersList


if __name__ == '__main__':
    num_cities: int = 10
    road_network = network_from_file('pokemon-center-test1.txt')
    print(road_network)
    result = can_be_made_tournament_ready(road_network, num_cities)
    print(f'result = {result}')

    # print(mst(road_network))
