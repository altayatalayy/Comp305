__doc__ = '''Comp 305 final project
Group No: 21
Members:
    Altay Atalay
    Andrew Bond

Project Name: Pokemon
'''

from util import *

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


@timer('Greedy algorithm : ')
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
    print('Testing with pokemon-center-test1.txt')
    road_network = network_from_file('pokemon-center-test1.txt')
    #print(road_network)
    result = can_be_made_tournament_ready(road_network, num_cities)
    print(f'result = {result}')

    print('\n\nTesting with pokemon-center-test2.txt')
    road_network = network_from_file('pokemon-center-test2.txt')
    result = can_be_made_tournament_ready(road_network, num_cities)
    print(f'result = {result}')

