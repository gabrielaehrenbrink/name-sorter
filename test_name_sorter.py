import unittest
from unittest.mock import patch
from name_sorter import FileReader, FileWriter, NameValidator, NameSorter
import os
import tempfile

class TestNameSorter(unittest.TestCase):

    def setUp(self):
        self.file_reader = FileReader()
        self.file_writer = FileWriter()
        self.name_validator = NameValidator()
        self.name_sorter = NameSorter()

    def test_sort_names(self):
        """
        Test that names are being sorted by last name.
        """
        names = ["Jane Doe", "Ada Lovelace", "Zoe Smith"]
        sorted_names = self.name_sorter.sort(names)
        self.assertEqual(sorted_names, ["Jane Doe", "Ada Lovelace", "Zoe Smith"], "Should sort names by last name")

    def test_sort_given_names(self):
        """
        Test that names are being sorted by last name and given names.
        """
        names = ["Jane Doe", "Ada Lovelace", "Zoe Smith", "John Smith"]
        sorted_names = self.name_sorter.sort(names)
        self.assertEqual(sorted_names, ["Jane Doe", "Ada Lovelace", "John Smith", "Zoe Smith"], "Should sort names by last name and given names")

    def test_sort_multiple_given_names(self):
        """
        Test that names are being sorted by last name and multiple given names.
        """
        names = ["Jane Mary Smith", "Ada Amy Abigail Smith", "John Paul Smith", "John Smith"]
        sorted_names = self.name_sorter.sort(names)
        self.assertEqual(sorted_names, ["Ada Amy Abigail Smith", "Jane Mary Smith", "John Paul Smith", "John Smith"], "Should sort names by last name and given names")

    def test_surname_only(self):
        """
        Test that a name with only a surname and no given names is considered invalid
        and not included in the sorted list.
        """
        names = ["Smith"]
        valid_names = self.name_validator.validate(names)
        self.assertEqual(valid_names, [], "Error: Invalid name on the list - 'Smith'.")

    def test_more_than_three_given_names(self):
        """
        Test that a name with more than three given names is considered invalid
        and not included in the sorted list.
        """
        names = ["John Jacob Jingleheimer Schmidt Smith"]
        valid_names = self.name_validator.validate(names)
        self.assertEqual(valid_names, [], "Error: Invalid name on the list - 'John Jacob Jingleheimer Schmidt Smith'.")

    def test_sort_repeated_names(self):
        """
        Test that names are being sorted by last name and given names when there is a repeated name
        """
        names = ["Jane Doe", "Ada Lovelace", "Zoe Smith", "John Smith", "John Smith"]
        sorted_names = self.name_sorter.sort(names)
        self.assertEqual(sorted_names, ["Jane Doe", "Ada Lovelace", "John Smith", "John Smith", "Zoe Smith"], "Should sort names by last name and given names even with repeated names")

    def test_read_names_from_file(self):
        with tempfile.NamedTemporaryFile(delete=False, mode='w') as tmp:
            tmp.write("Jane Doe\nAda Lovelace\nZoe Smith")
            tmp_name = tmp.name
        names = self.file_reader.read_from_file(tmp_name)
        os.remove(tmp_name)
        self.assertEqual(names, ["Jane Doe", "Ada Lovelace", "Zoe Smith"], "Should read names from file")

    def test_write_names_to_file(self):
        names = ["Jane Doe", "Ada Lovelace", "Zoe Smith"]
        with tempfile.NamedTemporaryFile(delete=False, mode='r+') as tmp:
            tmp_name = tmp.name
        self.file_writer.write_to_file(tmp_name, names)
        with open(tmp_name, 'r') as file:
            content = file.read().strip().split('\n')
        os.remove(tmp_name)
        self.assertEqual(content, names, "Should write names to file correctly")

if __name__ == '__main__':
    unittest.main()