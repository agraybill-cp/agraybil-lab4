import sys
import unittest
from typing import *
from dataclasses import dataclass
import math
# import matplotlib.pyplot as plt
# import numpy as np 
import random
import time
sys.setrecursionlimit(10**6)

from bst import *

TREES_PER_RUN : int = 10000


# find the height of a given tree
def height( input : BinTree) -> int:
    match input:
        case None:
            return 0
        case Node(left=l, right=r):
            return max(1 + height(l), 1 + height(r))
        

def random_tree(n : int) -> BinarySearchTree:
    a : BinarySearchTree = BinarySearchTree(lambda a, b: a < b, None)
    for _ in range(n):
        a = insert(a, random.random())
    return a

def run( n : int) -> None:
    t : float = time.time()
    tot_height : int = 0
    for _ in range(TREES_PER_RUN):
        a : BinarySearchTree = random_tree(n)
        tot_height += height(a.tree)
    print(tot_height/TREES_PER_RUN)
    print(time.time() - t)



def example_graph_creation() -> None:
# Return log-base-2 of 'x' + 5.
    def f_to_graph( x : float ) -> float:
        return math.log2( x ) + 5.0
    # here we're using "list comprehensions": more of Python's
    # syntax sugar.
    x_coords : List[float] = [ float(i) for i in range( 1, 100 ) ]
    y_coords : List[float] = [ f_to_graph( x ) for x in x_coords ]
    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array
    # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )
    plt.plot( x_numpy, y_numpy, label = 'log_2(x)' )
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Example Graph")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()

if (__name__ == '__main__'):
    #example_graph_creation()
    run(100)
