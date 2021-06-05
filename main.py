
__doc__ = '''Comp 305 final project
Group No: 21
Members:
    Altay Atalay

Project Name: Pokemon
'''

from util import *

def minKey(key, mstSet):
    # util function for prim algo
    #print(f'minkey key = {key}')
    _min = 100
    for v in range(len(key)):
        if 1 < _min and mstSet[v] == False:
            _min = key[v]
            min_index = v

    return min_index

def mst(tree : dict):
    #prims algorithm, returns a list of parents
    n = len(tree.keys())
    key = [100] * n
    parent = [None] * n
    key[0] = 0
    mstSet = [False] * n
    parent[0] = -1
    for i in range(n):
        u = minKey(key, mstSet)
        mstSet[u] = True
        for j in range(n):
            if list(tree.keys())[i] in  tree[list(tree.keys())[j]] and mstSet[j] == False and key[j] > 1:
                #print(i, j, u)
                key[j] = 1
                parent[j] = u

    rv = []
    #Convert indexes to city names
    for i in parent:
        if i == -1:
            continue
        if list(tree.keys())[i] not in rv:
            rv.append(list(tree.keys())[i] )

    return rv

def helper(selected_cities, road_network):
    # Recursive function to get a soluttion with minimum number of cities
    #print(len(selected_cities))
    if not type(selected_cities) in [list]:
        return

    if len(selected_cities) == 0:
        return

    if not check_correctness(selected_cities, road_network):
        return

    _min = len(selected_cities)
    _city = None
    _rv = selected_cities
    for city in selected_cities:
        sc = list(selected_cities)# create copy of selected cities
        sc.remove(city)
        rv = helper(sc, road_network)
        if rv == None:
            continue
        if len(rv) < _min:
            _min = len(rv)
            _rv = rv
            break

    #print(_rv)
    return _rv


@timer(message='Recursive algorithm : ')
def can_be_made_tournament_ready(road_network : dict, num_cities : int) -> list:
    '''The Algorithm
    '''
    if type(num_cities) not in [int, float] or num_cities < 0:
        raise ValueError(f'num cities must be a positive int')

    rv:list = []# return value, list of cities

    if num_cities == 0:
        return rv

    mst_list = mst(road_network)#Minimum Spanning Tree of our network

    # Get minimum number of cities
    min_list = helper(mst_list, road_network)
    if len(min_list) <= num_cities:
        rv = min_list

    return rv


if __name__ == '__main__':
    num_cities:int = 10

    print('Testing with pokemon-center-test1.txt')
    road_network = network_from_file('pokemon-center-test1.txt')
    result = can_be_made_tournament_ready(road_network, num_cities)
    print(f'result = {result}')

    print('\n\nTesting with pokemon-center-test2.txt')
    road_network = network_from_file('pokemon-center-test2.txt')
    result = can_be_made_tournament_ready(road_network, num_cities)
    print(f'result = {result}')


