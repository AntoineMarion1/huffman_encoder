#!/usr/bin/env python3

"""
Unzip a .ant file
"""

from os import getcwd

alphabet = [
    "a","b","c","d","e","f",
    "g","h","i","j","k","l",
    "m","n","o","p","q","r",
    "s","t","u","v","w","x",
    "y","z"
]
def get_code(file_to_unzip: str)->dict:
    """
    Retrieves the reversed code from an .ant file by reading the first few lines.
    """
    reversed_code = {}
    index = 0
    with open(file = file_to_unzip, encoding= "utf-8", mode = 'r') as f:
        assert f.readline() == "ANT\n", "Not a .ant file"
        f.readline()
        for line in f:
            if line == '\n':
                break
            reversed_code[line.split('\n')[0]] = alphabet[index]
            index += 1

    return reversed_code

def reverse_code(code: dict)->dict:
    """
    Reverse the code. The words in the code become the keys and the original
    symbols become the values.

    Parameters
    ---------
    - code: dict

    code to reverse

    Returns
    ---------
    - reversed_code: dict
    """
    reversed_code = {}
    for key in code:
        reversed_code[code[key]] = key
    return reversed_code


def get_next_char(file: str):
    with open(file = file, encoding = "utf-8", mode = "r") as f:
        for line in f:
            for ch in line:
                yield ch


def unzip(file_to_unzip: str, reversed_code: dict):
    """
    unzip
    """
    it = get_next_char(file_to_unzip)
    word = ''
    for ch in it:
        if word in reversed_code:
            print(reversed_code[word])
        else:
            word = word + ch


if __name__ == "__main__":
    f = "files/test.ant"
    reversed_code = get_code(f)
    print(reversed_code)
    unzip(f, reversed_code)
