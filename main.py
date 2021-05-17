
__doc__ = '''Comp 305 final project
Group No: 21
Members:
    Altay Atalay

Project Name: Pokemon
'''

def network_from_file(file_name : str) -> (dict, int):
    '''Create road network from input file
    '''
    num_cities:int = 0
    keys:list = [] # Cities
    values:'2d list' = [] # Connected Cities 2d list

    with open(file_name) as f:
        for line in f.readlines():
            if line[0] == "#":#Pass comments
                continue
            if line.strip() in ["", "\n"]:#Pass empty lines
                continue
            l = line.split(' ')
            city_name, x, y, *connected_cities = l
            x, y = int(x[1]), int(y[0])# Convert x and y from str to int
            connected_cities = [c.strip(',').strip('\n') for c in connected_cities]# Get rid of the ,

            keys.append(city_name)
            values.append(connected_cities)

    road_network:dict = {k : v for k,v in zip(keys, values)} # Create the road network usin keys and values
    return road_network, num_cities

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
    road_network, num_cities = network_from_file('pokemon-center-test1.txt')
    print(road_network)
    result = can_be_made_tournament_ready(road_network, num_cities)
    print(f'result = {result}')


