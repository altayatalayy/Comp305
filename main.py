
__doc__ = '''Comp 305 final project
Group No: 21
Members:
    Altay Atalay 64568

Project Name: Pokemon
'''

def can_be_made_tournament_ready(road_network : dict, num_cities : int) -> list:
    '''The Algorithm
    '''
    if type(num_cities) not in [int, float] or num_cities < 0:
        raise ValueError(f'num cities must be a positive int')

    rv:list = []# return value, list of cities

    if num_cities == 0:
        return rv

    return rv


if __name__ == '__main__':
    num_cities:int = 0
    keys:list = [] # Cities
    values:'2d list' = [] # Connected Cities 2d list

    road_network:dict = {k : v for k,v in zip(keys, values)} # Create the road network usin keys and values
    result = can_be_made_tournament_ready(road_network, num_cities)
    print(f'result = {result}')


