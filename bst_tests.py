import sys
import unittest
from typing import * # type:ignore
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *

def int_comes_before(a : int, b : int) -> bool:
    return a < b

def str_comes_before(a : str, b : str) -> bool:
    return a.lower() < b.lower()


@dataclass(frozen=True)
class Point2:
    x : float
    y : float

def euclidean_comes_before(a : Point2, b : Point2) -> bool:
    dist_a : float = (a.x ** 2 + a.y **2) ** 1/2
    dist_b : float = (b.x ** 2 + b.y **2) ** 1/2
    return dist_a < dist_b


class BSTTests(unittest.TestCase):
    def test_is_empty(self):
        a : BinarySearchTree = BinarySearchTree(int_comes_before, None)
        b : BinarySearchTree = BinarySearchTree(int_comes_before, Node(4, None, None))
        self.assertTrue(is_empty(a))
        self.assertFalse(is_empty(b))

    def test_insert_int(self):
        a : BinarySearchTree = BinarySearchTree(int_comes_before, None)
        a = insert(a, 5)
        self.assertEqual(a.tree, Node(5, None, None))
        a = insert(a, 8)
        self.assertEqual(a.tree, Node(5, None, Node(8, None, None)))
        a = insert(a, 3)
        a = insert(a, 1)
        self.assertEqual(a.tree, Node(5, Node(3, Node(1, None, None), None), Node(8, None, None)))

    def test_insert_str(self):
        a : BinarySearchTree = BinarySearchTree(str_comes_before, None)
        a = insert(a, "e")
        self.assertEqual(a.tree, Node("e", None, None))
        a = insert(a, "H")
        self.assertEqual(a.tree, Node("e", None, Node("H", None, None)))
        a = insert(a, "c")
        a = insert(a, "A")
        self.assertEqual(a.tree, Node("e", Node("c", Node("A", None, None), None), Node("H", None, None)))

    def test_insert_euclid(self):
        a : Point2 = Point2(1,1) # sqrt2
        b : Point2 = Point2(2,1) # sqrt5
        c : Point2 = Point2(3, 4) # 5
        d : Point2 = Point2(-12, -5) # 13

        tree : BinarySearchTree = BinarySearchTree(euclidean_comes_before, None)

        tree = insert(tree, a)
        self.assertEqual(tree.tree, Node(a, None, None))
        tree = insert(tree, c)
        self.assertEqual(tree.tree, Node(a, None, Node(c, None, None)))
        tree = insert(tree, b)
        self.assertEqual(tree.tree, Node(a, None, Node(c, Node(b, None, None), None)))
        tree = insert(tree, d)
        self.assertEqual(tree.tree, Node(a, None, Node(c, Node(b, None, None), Node(d, None, None))))




    def test_lookup_int(self):
        a : BinarySearchTree = BinarySearchTree(int_comes_before, Node(5, Node(3, Node(1, None, None), None), Node(8, None, None)))
        self.assertTrue(lookup(a, 5))
        self.assertTrue(lookup(a, 1))
        self.assertFalse(lookup(a, 15))
    def test_lookup_str(self):
        a : BinarySearchTree = BinarySearchTree(int_comes_before, Node("e", Node("c", Node("A", None, None), None), Node("H", None, None)))
        self.assertTrue(lookup(a, "e"))
        self.assertTrue(lookup(a, "A"))
        self.assertFalse(lookup(a, "m"))
        self.assertFalse(lookup(a, "E")) # This should be false but the reasoning why it is actually false is kind of strange

    def test_lookup_euc(self):
        a : Point2 = Point2(1,1) # sqrt2
        b : Point2 = Point2(2,1) # sqrt5
        c : Point2 = Point2(3, 4) # 5
        d : Point2 = Point2(-12, -5) # 13
        e : Point2 = Point2(5, 5)
        tree : BinarySearchTree = BinarySearchTree(euclidean_comes_before, Node(a, None, Node(c, Node(b, None, None), Node(d, None, None))))

        self.assertTrue(lookup(tree, a))
        self.assertTrue(lookup(tree, b))
        self.assertFalse(lookup(tree, e))


if (__name__ == '__main__'):
    unittest.main()