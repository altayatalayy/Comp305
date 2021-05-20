
import unittest

from main import *
from main import can_be_made_tournament_ready as algo

class TestAlgo(unittest.TestCase):

    def test_inputs(self):
        print('testing invalid values')
        self.assertRaises(ValueError, algo, {}, -1)

    def test_input_from_fille(self):
        print('test input from file')
        road_network = network_from_file('pokemon-center-test1.txt')
        self.assertEqual(type(road_network), dict)

    def test_mst(self):
        print('check prims algo')
        road_network = network_from_file('pokemon-center-test1.txt')
        _mst = mst(road_network)
        self.assertEqual(check_correctness(_mst, road_network), True)

    def test_correctness(self):
        print('testing correctness')
        num_cities = 10
        road_network = network_from_file('pokemon-center-test1.txt')
        result = can_be_made_tournament_ready(road_network, num_cities)# get nodes to place center

        #Check results type
        self.assertEqual(type(result), list)
        for r in result:
            self.assertEqual(type(r), str)

        self.assertEqual(check_correctness(result, road_network), True)


if __name__ == '__main__':
    unittest.main()
