#
import unittest
from src.homework.h_strings import get_hamming_distance
from src.homework.h_strings import get_dna_complement

class Test_Config(unittest.TestCase):
    def get_hamming_distance(self):
        self.assertEqual(7, get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))

    def get_dna_complement(self):
        self.assertEqual("AAAACCCGGT", get_dna_complement("ACCGGGTTTT"))