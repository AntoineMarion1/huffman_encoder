#!/usr/bin/env python3

"""
Analyze a text file.
"""

def analyze_file(file_name: str):
    """
    Analyze a file which contains text.

    Parameters
    ---------

    - file_name: str

    The file to analyze. Should only contain letters.

    Returns
    --------
    - letters_dict: dict

    A dictionary containing the number of occurences of each letter.
    """
    letters_count = {
        "a": 0,"b": 0,"c": 0,"d": 0,"e": 0,"f": 0,
        "g": 0,"h": 0,"i": 0,"j": 0,"k": 0,"l": 0,
        "m": 0,"n": 0,"o": 0,"p": 0,"q": 0,"r": 0,
        "s": 0,"t": 0,"u": 0,"v": 0,"w": 0,"x": 0,
        "y": 0,"z": 0,
    }

    with open(file = file_name, encoding = "utf-8", mode = "r") as f:
        for line in f:
            for ch in line:
                ascii_code = analyze_char(ch)
                if ascii_code is not None:
                    #-97 because the ascii code of 'a' is 97
                    letters_count[ch.lower()] += 1
    return letters_count

def analyze_char(ch: str):
    """
    Returns the ascci code if the character is a letter, else None.
    Lower and upper case are not different.

    Parameters:
    --------
    - ch: str

    A string containing only one character.

    Returns:
    --------
    - ascii_code: int

    Ascii code of the char.
    """
    ascii_code = 0
    assert len(ch) == 1, "Size of the char is not one."
    if ord(ch) >= 65 and ord(ch) <= 90:
        ascii_code = ord(ch)+32
    elif ord(ch) >= 97 and ord(ch)<= 122:
        ascii_code = ord(ch)
    else:
        ascii_code = None

    return ascii_code
