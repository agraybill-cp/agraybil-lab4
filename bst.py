import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)


BinTree : TypeAlias = Optional["Node"]

@dataclass(frozen=True)
class Node:
    val : Any
    left : BinTree
    right : BinTree

@dataclass(frozen=True)
class BinarySearchTree:
    comes_before : Callable[[Any, Any], bool]
    tree : BinTree

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





def largest_value( input : BinTree, comes_before : Callable[[Any, Any], bool]) -> Any:
    pass

def delete_largest( input : BinTree) -> BinTree:
    pass

def delete_helper( input : BinTree, comes_before : Callable[[Any,Any], bool], val : Any) -> BinarySearchTree:
    match input:
        case None:
            return None # should never happen
        case Node(v, l, r):
            if comes_before(val, v):
                return delete_helper(l, comes_before, val)
            if comes_before(v, val):
                return delete_helper(r, comes_before, val)
            else:
                left_max : Any = largest_value(input, comes_before)
                new_left : BinTree = delete_largest(input)
                return BinarySearchTree(comes_before, new_left)



# delete an instance of the given value from the given tree
def delete( input_tree : BinarySearchTree, val : Any) -> BinarySearchTree:
    if not lookup(input_tree, val):
        return input_tree
    return delete_helper(input_tree.tree, input_tree.comes_before, val)

def ex_comes_before( a : int, b : int) -> bool:
    return a < b

