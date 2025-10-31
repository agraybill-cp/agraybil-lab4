import sys
import unittest
from typing import * # type:ignore
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *

def ex_comes_before(a : int, b : int) -> bool:
    return a < b

class BSTTests(unittest.TestCase):
    def test_example(self):
        pass
    def test_is_empty(self):
        a : BinarySearchTree = BinarySearchTree(ex_comes_before, None)
        b : BinarySearchTree = BinarySearchTree(ex_comes_before, Node(4, None, None))
        self.assertTrue(is_empty(a))
        self.assertFalse(is_empty(b))

    def test_insert(self):
        a : BinarySearchTree = BinarySearchTree(ex_comes_before, None)
        a = insert(a, 5)
        self.assertEqual(a.tree, Node(5, None, None))
        a = insert(a, 8)
        self.assertEqual(a.tree, Node(5, None, Node(8, None, None)))
        a = insert(a, 3)
        a = insert(a, 1)
        self.assertEqual(a.tree, Node(5, Node(3, Node(1, None, None), None), Node(8, None, None)))

    def test_lookup(self):
        a : BinarySearchTree = BinarySearchTree(ex_comes_before, Node(5, Node(3, Node(1, None, None), None), Node(8, None, None)))
        self.assertTrue(lookup(a, 5))
        self.assertTrue(lookup(a, 1))
        self.assertFalse(lookup(a, 15))


if (__name__ == '__main__'):
    unittest.main()