
import unittest

import main

f = main.can_be_made_tournament_ready

class TestAlgo(unittest.TestCase):

    def test(self):
        # test negative num cities
        self.assertRaises(ValueError, f, {}, -1)


if __name__ == '__main__':
    unittest.main()
