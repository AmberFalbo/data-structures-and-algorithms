import pytest
from challenges.fizz_buzz_tree.fizz_buzz_tree import K_ary_Tree, K_node, FizzBuzzTree


# ********** K-ary Tree **************

def test_can_return_fizzybuzzy_tree():
    k_tree = K_ary_Tree()
    k1 = K_node(30)
    k2 = K_node(2)
    k3 = K_node(5)
    k4 = K_node(7)
    k5 = K_node(20)
    k6 = K_node(9)
    k7 = K_node(8)
    k8 = K_node(4)
    k9 = K_node(12)
    k10 = K_node(15)
    k11 = K_node(6)
    k12 = K_node(10)
    k13 = K_node(3)
    # **order_connections**
    k13.children.append(k12)
    k13.children.append(k11)
    k13.children.append(k10)
    k12.children.append(k2)
    k12.children.append(k3)
    k12.children.append(k4)
    k11.children.append(k5)
    k11.children.append(k6)
    k6.children.append(k1)
    k10.children.append(k7)
    k10.children.append(k8)
    k10.children.append(k9)
    k_tree.root = k13

    fizzy = FizzBuzzTree()
    fizz_tree = fizzy.pre_fizz_buzz(k_tree)
    actual = fizz_tree.pre_order()
    expected = ["Fizz", "Buzz", "2", "Buzz", "7", "Fizz", "Buzz", "Fizz", "FizzBuzz", "Buzz", "8", "4", "Fizz"]
    assert actual == expected


def test_k_ary_tree_pre_order_traverse():
    k_tree = K_ary_Tree()
    k1 = K_node(30)
    k2 = K_node(2)
    k3 = K_node(5)
    k4 = K_node(7)
    k5 = K_node(20)
    k6 = K_node(9)
    k7 = K_node(8)
    k8 = K_node(4)
    k9 = K_node(12)
    k10 = K_node(15)
    k11 = K_node(6)
    k12 = K_node(10)
    k13 = K_node(3)
    # **order_connections**
    k13.children.append(k12)
    k13.children.append(k11)
    k13.children.append(k10)
    k12.children.append(k2)
    k12.children.append(k3)
    k12.children.append(k4)
    k11.children.append(k5)
    k11.children.append(k6)
    k6.children.append(k1)
    k10.children.append(k7)
    k10.children.append(k8)
    k10.children.append(k9)
    k_tree.root = k13
    actual = k_tree.pre_order()
    expected = [3, 10, 2, 5, 7, 6, 20, 9, 30, 15, 8, 4, 12]
    assert actual == expected