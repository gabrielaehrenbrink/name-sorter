import unittest
from unittest.mock import patch
from name_sorter import sort_names, read_names_from_file, write_names_to_file
import os
import tempfile

class TestNameSorter(unittest.TestCase):

    def test_sort_names(self):
        """
        Test that names are being sorted by last name.
        """
        names = ["Jane Doe", "Ada Lovelace", "Zoe Smith"]
        sorted_names = sort_names(names)
        self.assertEqual(sorted_names, ["Jane Doe", "Ada Lovelace", "Zoe Smith"], "Should sort names by last name")

    def test_sort_given_names(self):
        """
        Test that names are being sorted by last name and given names.
        """
        names = ["Jane Doe", "Ada Lovelace", "Zoe Smith", "John Smith"]
        sorted_names = sort_names(names)
        self.assertEqual(sorted_names, ["Jane Doe", "Ada Lovelace", "John Smith", "Zoe Smith"], "Should sort names by last name and given names")

    def test_sort_multiple_given_names(self):
        """
        Test that names are being sorted by last name and given names.
        """
        names = ["Jane Mary Smith", "Ada Amy Abigail Smith", "John Paul Smith", "John Smith"]
        sorted_names = sort_names(names)
        self.assertEqual(sorted_names, ["Ada Amy Abigail Smith", "Jane Mary Smith", "John Paul Smith", "John Smith"], "Should sort names by last name and given names")

    def test_surname_only(self):
        """
        Test that a name with only a surname and no given names is considered invalid
        and not included in the sorted list.
        """
        names = ["Smith"]
        expected = []
        result = sort_names(names)
        self.assertEqual(result, expected, "A name with only a surname and no given name should be considered invalid.")

    def test_more_than_three_given_names(self):
        """
        Test that a name with more than three given names is considered invalid
        and not included in the sorted list.
        """
        names = ["John Jacob Jingleheimer Schmidt Smith"]
        expected = []
        result = sort_names(names)
        self.assertEqual(result, expected, "A name must have no more than 3 given names and a surname.")

    def test_read_names_from_file(self):
        with tempfile.NamedTemporaryFile(delete=False, mode='w') as tmp:
            tmp.write("Jane Doe\nAda Lovelace\nZoe Smith")
            tmp_name = tmp.name
        names = read_names_from_file(tmp_name)
        os.remove(tmp_name)
        self.assertEqual(names, ["Jane Doe", "Ada Lovelace", "Zoe Smith"], "Should read names from file")

    def test_write_names_to_file(self):
        names = ["Jane Doe", "Ada Lovelace", "Zoe Smith"]
        with tempfile.NamedTemporaryFile(delete=False, mode='r+') as tmp:
            tmp_name = tmp.name
        write_names_to_file(tmp_name, names)
        with open(tmp_name, 'r') as file:
            content = file.read().strip().split('\n')
        os.remove(tmp_name)
        self.assertEqual(content, names, "Should write names to file correctly")

if __name__ == '__main__':
    unittest.main()