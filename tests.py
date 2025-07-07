# tests.py

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


class TestGetFileInfo(unittest.TestCase):
    def test_get_file_info(self):
        print(get_file_content("calculator", "main.py"))
        print(get_file_content("calculator", "pkg/calculator.py"))
        print(get_file_content("calculator", "/bin/cat"))
        

if __name__ == "__main__":
    unittest.main()
