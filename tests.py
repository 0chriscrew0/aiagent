# tests.py

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


class TestGetFileInfo(unittest.TestCase):
    def test_get_file_info(self):
        print(run_python_file("calculator", "main.py"))
        print(run_python_file("calculator", "tests.py"))
        print(run_python_file("calculator", "../main.py"))
        print(run_python_file("calculator", "nonexistent.py"))

if __name__ == "__main__":
    unittest.main()
