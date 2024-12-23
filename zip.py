#!/usr/bin/env python3

"""
Zip a text file in .ant format. This format uses Huffman coding.
"""

import sys
from analyze import analyze_file
from huffman import create_huffman_code, average_lenght

def get_code(file_to_zip: str):
    """
    Retrieves the Huffman code corresponding to the file passed in parameter.

    Parameters
    ---------
    - file_to_zip: str

    file made up of letters whose coding we want to know. We test if the file
    exists in the working directory.

    Returns
    ---------
    - huffman_code: dict

    A dictionary containing the binary encoding of each character in the starting alphabet.
    """
    try:
        d = analyze_file(file_to_zip)
        code = create_huffman_code(d)
        print(code)
        print("Average lenght: ")
        print(average_lenght(d, code))
        return code

    except FileNotFoundError:
        print("The file does not exist.")
        sys.exit()

def get_output_file_name(file_to_zip: str):
    """
    Returns the path to the file corresponding to the ziped file_to_zip.

    Parameters
    ---------
    - file_to_zip: str

    File whose ziped file name we want to know
    """
    file = ''
    for ch in file_to_zip:
        if ch == '.':
            break
        file = file+ch

    return file + ".ant"


def zip(file_to_zip: str, code: dict):
    """
    a faireeeeee
    """
    output_file = get_output_file_name(file_to_zip)
    sorted_code = dict(sorted(code.items()))
    print(sorted_code)

    with open(file = output_file, encoding = "utf-8", mode = 'w') as f:
        print("ANT", file = f)
        print('', file = f)
        for symbol in sorted_code:
            print(sorted_code[symbol], file = f)
        print('', file = f)

        with open(file = file_to_zip, encoding = 'utf-8', mode = 'r') as f_to_zip:
            for line in f_to_zip:
                for ch in line:
                    ch = ch.lower()
                    if ch == ' ':
                        print(' ', file = f, end = '')
                    elif ch == '\n':
                        print('', file = f)
                    else:
                        print(code[ch], file = f, end = '')

if __name__ == "__main__":

    args = sys.argv
    if len(args) != 2:
        print("Usage: ./zip.py <file_to_zip>")
        sys.exit()

    file_to_zip = "files/"+args[1]

    assert isinstance(file_to_zip, str), "<file_to_zip> should be a file_name"

    code = get_code(file_to_zip)
    zip(file_to_zip,code)
