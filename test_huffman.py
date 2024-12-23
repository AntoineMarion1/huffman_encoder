#!/usr/bin/env python3

"""
Test huffman.py
"""

from extension.huffman import Node
from extension.huffman import dic_to_nodes
from extension.huffman import find_two_minimal_weight_nodes
from extension.huffman import group_two_nodes


def test_dic_to_nodes():
    print("----- TEST dic_to_nodes(dic: dict) -----")
    dic = {"a": 0, "b": 1, "c": 2, "d": 3}
    nodes_list = dic_to_nodes(dic)
    for i in range(len(nodes_list)):
        assert nodes_list[i].weight == i, "Incorrect weight"
    assert nodes_list[0].letters == {"a": ''}, "Incorrect symbol"
    assert nodes_list[1].letters == {"b": ''}, "Incorrect symbol"
    assert nodes_list[2].letters == {"c": ''}, "Incorrect symbol"

    print("TESTS OK")

def test_find_two_minimal_weight_nodes():
    print("----- TEST two_minimal_weight_nodes(nodes_list: list) -----")
    a = Node("a", 3)
    b = Node("b", 4)
    c = Node("c", 5)
    nodes_list_1 = [a, b, c]
    assert find_two_minimal_weight_nodes(nodes_list_1) == (b, a)
    nodes_list_2 = [b, a]
    assert find_two_minimal_weight_nodes(nodes_list_2) == (b, a)
    print("TESTS OK")

def test_group_two_nodes():
    print("----- TEST groupe_two_nodes(node_1: Node, node_2: Node, nodes_list: list) -----")
    a = Node("a", 3)
    b = Node("b", 4)
    c = Node("c", 5)
    nodes_list_1 = [a, b, c]
    new_node = Node("a", 7)
    new_node.letters = {"a": '0', "b": "1"}
    group_two_nodes(a, b, nodes_list_1)
    assert nodes_list_1[1].letters == new_node.letters, "Letters are different"
    assert nodes_list_1[1].weight == new_node.weight, "Weights are different"
    print("TESTS OK")

if __name__ == '__main__':
    test_dic_to_nodes()
    test_find_two_minimal_weight_nodes()
    test_group_two_nodes()
