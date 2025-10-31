import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
import random


BinTree : TypeAlias = Optional["Node"]

@dataclass(frozen=True)
class Node:
    val : Any
    left : BinTree
    right : BinTree

    def __str__(self):
        return f"v: {self.val}, l: ({self.left}), r: ({self.right})"

@dataclass(frozen=True)
class BinarySearchTree:
    comes_before : Callable[[Any, Any], bool]
    tree : BinTree
    def __str__(self):
        return str(self.tree)

# Returns True if the given binary search tree is empty
def is_empty( input_tree : BinarySearchTree) -> bool:
    return input_tree.tree is None


# Helper function for insert function
def insert_helper( tree : BinTree, comes_before : Callable[[Any, Any], bool], val : Any) -> BinTree:
    match tree:
        case None:
            return Node(val, None, None)
        case Node(v, l, r):
            if (comes_before(val, v)): # smaller than node
                return Node(v, insert_helper(l, comes_before, val), r)
            else:
                return Node(v, l, insert_helper(r, comes_before, val))


# Inserts a given valye into a given BinarySearchTree 
# as described by the BST's comes_before function 
def insert( input_tree : BinarySearchTree, val : Any) -> BinarySearchTree:
    return BinarySearchTree(input_tree.comes_before, insert_helper(input_tree.tree, input_tree.comes_before, val))

# Helper functino for the lookup function
def lookup_helper( tree : BinTree, comes_before : Callable[[Any, Any], bool], val : Any) -> bool:
    match tree:
        case None:
            return False
        case Node(v, l, r):
            if comes_before(val, v):
                return lookup_helper(l, comes_before, val)
            if comes_before(v, val):
                return lookup_helper(r, comes_before, val)
            else:
                return True



# Returns true if a given value was ina given BST
def lookup( input_tree : BinarySearchTree, val : Any) -> bool:
    return lookup_helper(input_tree.tree, input_tree.comes_before, val)


# finds the largest value in a given tree
def largest_value( input : BinTree) -> Any:
    match input:
        case None:
            return None
        case Node(val = v, right = r):
            if r is None:
                return v
            return largest_value(r) 

# deletes the largest value (bottom right) from a given tree 
def delete_largest( input : BinTree) -> BinTree:
    match input:
        case None:
            return None
        case Node(v, l, r):
            if r is None:
                return l
            return Node(v,l, delete_largest(r))

# Main helper function for delete function
def delete_helper( input : BinTree, comes_before : Callable[[Any,Any], bool], val : Any) -> BinTree:
    match input:
        case None:
            return None
        case Node(v, l, r):
            if comes_before(val, v):
                print("left")
                return Node(v, delete_helper(l, comes_before, val), r)
            if comes_before(v, val):
                print("right")
                return Node(v, l, delete_helper(r, comes_before, val))
            else:
                print("equal")
                left_max : Any = largest_value(l)
                print(left_max)
                new_left : BinTree = delete_largest(l)
                print(new_left)
                return Node(left_max, new_left, r)

# find the height of a given tree
def height( input : BinTree) -> int:
    match input:
        case None:
            return 0
        case Node(left=l, right=r):
            return max(1 + height(l), 1 + height(r))
        

def random_tree(n : int) -> BinarySearchTree:
    a : BinarySearchTree = BinarySearchTree(lambda a, b: a < b, None)
    for i in range(n):
        a = insert(a, random.random())


# delete an instance of the given value from the given tree
def delete( input_tree : BinarySearchTree, val : Any) -> BinarySearchTree:
    if not lookup(input_tree, val):
        return input_tree
    return BinarySearchTree(input_tree.comes_before, delete_helper(input_tree.tree, input_tree.comes_before, val))
