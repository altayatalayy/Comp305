
from functools import wraps

def timer(message=""):
    def inner(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            import time
            t0 = time.time()
            rv = f(*args, **kwargs)
            t1 = time.time()
            print(f'{message}Elapsed time for {f.__name__}: {t1 - t0:7.5f} s')
            return rv
        return wrapper
    return inner

def check_correctness(selected_cities, road_network):
    # check if the solution satisfies the problem
    has_center = {k : False for k in road_network.keys()}
    near_center = dict(has_center)

    #Mark cities with centers
    for city_name in selected_cities:
        has_center[city_name] = True#if there is pokecenter

    # if any of the adjacent cities has center mark this city as near center
    for k in road_network.keys():
        for adj_city in road_network[k]:
            if has_center[adj_city]:
                near_center[k] = True

    #print(f'{has_center}, {near_center}')
    rv = all([h or n for h,n in zip(has_center.values(), near_center.values())])
    return rv


def network_from_file(file_name : str) -> dict:
    '''Create road network from input file
    '''
    keys:list = [] # Cities
    values:'2d list' = [] # Connected Cities 2d list

    with open(file_name) as f:
        for line in f.readlines():
            if line[0] == "#":#Pass comments
                continue
            if line.strip() in ["", "\n"]:#Pass empty lines
                continue
            l = line.split(':')
            *city_name, x, y, = l[0].split(' ')
            city_name = ' '.join(city_name).strip(' ')
            x, y = int(x[1]), int(y[0])# Convert x and y from str to int
            connected_cities = l[1].strip(' ').split(',')
            connected_cities = [c.strip(' \n') for c in connected_cities]# Get rid of the ,

            keys.append(city_name)
            values.append(connected_cities)

    road_network:dict = {k : v for k,v in zip(keys, values)} # Create the road network usin keys and values
    return road_network


