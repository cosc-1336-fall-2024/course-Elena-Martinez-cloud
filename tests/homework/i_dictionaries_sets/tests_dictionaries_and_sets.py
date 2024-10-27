#
import unittest
from src.homework.i_dictionaries_sets.dictionary import get_p_distance, test_config
from src.homework.i_dictionaries_sets.dictionary import get_p_distance_matrix

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    #After the line that begins with class write a test case function test_p_distance
    #Test that get_p_distance with parameter values ['T','T','T','C','C','A','T','T','T','A']
    #and ['G','A','T','T','C','A','T','T','T','C'] that returns .4.
    def test_p_distance(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']
        expected_distance = 0.4

        actual_distance = get_p_distance(list1, list2)

        self.assertEqual(actual_distance, expected_distance)

    #Test case function test_get_p_distance_matrix
    #Test that get_p_distance matrix with parameter value
    def test_get_p_distance_matrix (self):
        dna_list =[['T','T','T','C','C','A','T','T','T','A'],
                   ['G','A','T','T','C','A','T','T','T','C'],
                   ['T','T','T','C','C','A','T','T','T','T'],
                   ['G','T','T','C','C','A','T','T','T','A']
        ]
        expected_matrix = [[0.0, 0.4, 0.1, 0.1],
                           [0.4, 0.0, 0.4, 0.3],
                           [0.1, 0.4, 0.0, 0.2],
                           [0.1, 0.3, 0.2, 0.0]
        ]
        actual_matrix = get_p_distance_matrix(dna_list)

        for i in range(len(expected_matrix)):
            self.assertEqual(actual_matrix[i], expected_matrix[i])
 
