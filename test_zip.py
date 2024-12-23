#!/usr/bin/env python3

"""
Test zip file
"""

from zip import get_output_file_name

def test_get_output_file_name():
    print("----- TEST get_output_file_name(file_to_zip: str) -----")
    file_to_zip = "files/test.txt"
    assert get_output_file_name(file_to_zip) == "files/test.ant"
    print("TESTS OK")

if __name__ == "__main__":
    test_get_output_file_name()
