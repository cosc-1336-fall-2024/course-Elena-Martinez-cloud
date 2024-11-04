import unittest
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value, test_config
from src.homework.g_lists_and_tuples.lists import get_highest_list_value

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    #1-Test that in the list 8, 10, 1, 50, 20 the get_lowest_list_values returns 1
    def test_get_lowest_list_value(self):
        numbers = [8, 10, 1, 50, 20]
        self.assertEqual(get_lowest_list_value(numbers), 1, "Lowest value is 1")
    
    # 2-Test that in the list 8, 10, 1, 50, 20 the get_highest_list_values returns 50
    def test_get_highest_list_value(self):
        numbers = [8, 10, 1, 50, 20]
        self.assertEqual (get_highest_list_value(numbers), 50, "Highest value is 50")