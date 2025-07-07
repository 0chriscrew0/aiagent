# tests.py

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


class TestGetFileInfo(unittest.TestCase):
    def test_get_file_info(self):
        print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
        print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
        print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
        

if __name__ == "__main__":
    unittest.main()
