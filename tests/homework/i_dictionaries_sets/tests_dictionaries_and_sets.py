import unittest
from src.homework.i_dictionaries_sets.dictionary import test_config, add_inventory
from src.homework.i_dictionaries_sets.dictionary import remove_inventory_widget

class Test_Config(unittest.TestCase):
    def test_configuration(self):
        self.assertEqual(True, test_config())

#Test case test_add_inventory
#Write to assert that adding Widget1 with quantity of 10 to the inventory_dictionary 
# inserts the Widget1 with value of 10 for quantity.
#Write another assertion to test that adding Widget1 with quantity of 25 updates 
# the existing Widget1 item quantity to 35.
#Write another assertion to test that adding Widget1 with quantity of -10 updates 
# the existing Widget1 item quantity to 25.

    def test_add_inventory(self):
        inventory_dictionary = {}

        add_inventory(inventory_dictionary, 'Widget1', 10)
        self.assertEqual(inventory_dictionary['Widget1'], 10)

        add_inventory(inventory_dictionary, 'Widget1', 25)
        self.assertEqual(inventory_dictionary['Widget1'], 35)

        add_inventory(inventory_dictionary, 'Widget1', -10)
        self.assertEqual(inventory_dictionary['Widget1'], 25)

#Test case test_remove_inventory_widget
#Write a test case add two widgets(widget1 and widget2 with quantities of your choice).
#Remove widget1. Test that the length of dictionary is 1 and that widget2 still exists.
    def test_remove_inventory_widget(self):
        inventory_dictionary = {}

        add_inventory(inventory_dictionary, 'Widget1', 10)
        add_inventory(inventory_dictionary, 'Widget2', 5)

        result = remove_inventory_widget(inventory_dictionary, 'Widget1')
        self.assertEqual(result, 'Record deleted')

        self.assertEqual(len(inventory_dictionary), 1)

        self.assertIn('Widget2', inventory_dictionary)
        self.assertEqual(inventory_dictionary['Widget2'], 5)