#!/usr/bin/env python3

"""
Create a Huffman binary code.
"""

import math


class Node:
    """
    A node in a Huffman tree. The attributes of a node are:

    - A dictionary containing the binary encoding of all characters
    accessible from this node.
    - A weight corresponding to the sum of the weights of all the characters
    accessible from this node.
    """
    def __init__(self, letter: str, weight: float):
        self.letters = {letter:''}
        self.weight = weight

    def __str__(self):
        return f"{self.letters}"

def dic_to_nodes(dic:dict):
    """
    Transforms a dictionary containing the number of occurrences of each character
    (or the percentage of occurrences) into a list of leaf nodes of a Huffman tree.

    Parameters
    ----------
    - dic: dict

    Returns
    ---------
    - nodes_list: list
    """
    nodes_list = []
    for char in dic:
        nodes_list.append(Node(char, dic[char]))
    return nodes_list

def find_two_minimal_weight_nodes(nodes_list: list):
    """
    Returns a tuple containing references to the two nodes with the lowest weight.
    First the node with the highest weight is returned, then the node with the
    lowest weight.

    Parameters
    ----------
    - nodes_list: dict

    Returns
    ---------
    - min_1: Node
    - min_2: Node
    """
    if len(nodes_list) < 2:
        raise ValueError("The list is not long enough")

    min_2 = Node('?', math.inf) # the second minimal value
    min_1 = Node('?', math.inf) #the minimal value
    # min_1;weight <= min_2.weight

    for node in nodes_list:

        assert isinstance(node, Node), "Object is not a Node"

        if node.weight > min_1.weight and node.weight > min_2.weight:
            pass
        elif node.weight >= min_1.weight and node.weight <= min_2.weight:
            min_2 = node
        elif node.weight <= min_1.weight and node.weight <= min_2.weight:
            min_2 = min_1
            min_1 = node

    return min_2, min_1

def group_two_nodes(left_node: Node, right_node: Node, nodes_list: list)->None:
    """
    Regroups two nodes into one and updates the list of nodes. Grouping
    two nodes means creating a new node whose weight is the sum of its two
    children and whose dictionary of letters is the concatenation of the dict.
    When we update the dictionary of letters, we add a binary character at the
    beginning of the string, corresponding to: 0 for the left child,
    1 for the right child.

    Parameters
    ---------
    - left_node: Node

    Higher weight node.

    - right_node: Node

    Lower weight node.
    """
    assert left_node in nodes_list, "Left node is not in the nodes list"
    assert right_node in nodes_list, "Right node is not in the nodes list"

    new_weight = left_node.weight + right_node.weight
    new_dict = {}

    for letter in left_node.letters:
        new_dict[letter] = "0" + left_node.letters[letter]
    for letter in right_node.letters:
        new_dict[letter] = "1" + right_node.letters[letter]

    # create a new node
    new_node = Node("", new_weight)
    new_node.letters = new_dict

    # update the list
    nodes_list.remove(left_node)
    nodes_list.remove(right_node)
    nodes_list.append(new_node)

def create_huffman_code(dic: dict):
    """
    Creates a Huffman binary code from a dictionary of character frequencies
    (or occurrences or probabilities of occurrence).

    Parameters
    ---------
    - dic: dict

    The dictionary must be of the following form: {‘character’: frequency_of_character}.

    Returns
    ---------
    - huffman code: dict

    A dictionary containing the binary encoding of each character in the starting alphabet.
    """
    nodes_list = dic_to_nodes(dic)
    while(len(nodes_list)) > 1:
        min_1, min_2 = find_two_minimal_weight_nodes(nodes_list)
        group_two_nodes(min_1, min_2, nodes_list)

    return nodes_list[0].letters

def average_lenght(dic: dict, huffman_code: dict):
    """
    Computes the average length of the Huffman code, using the symbol frequencies.
    """
    total_symbols = 0
    for ch in dic:
        total_symbols += dic[ch]

    average_lenght = 0
    for ch in huffman_code:
        average_lenght += len(huffman_code[ch]) * dic[ch]/total_symbols

    return average_lenght


if __name__ == '__main__':
    d = {"a":5, "b": 5, "c": 3, "d": 2, "e": 1}
    print(create_huffman_code(d))
