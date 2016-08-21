# Primitive types: write a program that takes as input an integer, N, and prints
# all the integers from 1 to N, replacing numbers divisible by 3 with "fizz", numbers divisible by
# 5 with "buzz", and numbers divisible by both with "fizz buzz".
# 
# Complexity:
# Runtime: O(n)
# Space: O(1)
def fizz_buzz(N=15):
    print("printing fizz buzz up to " + str(N))
    for x in range(1, N + 1):
        if x % 5 == 0 and x % 3 == 0:
            print(str(x) + ": fizz buzz")
        elif x % 3 == 0:
            print(str(x) + ": fizz")
        elif x % 5 == 0:
            print(str(x) + ": buzz")

# Arrays: Write a program that tests if a 2D square array is symmetric about the diagonal
# from (0,0) to (n-1,n-1).
def is_symmetric(matrix):
    pass

# Strings: Write a program to find the longest substring that consists of a single
# character in an input string.
def find_longest_single_char_substring(input_string, version = 0):
    if version == 0:
        # Runtime:
        # Space:
        curr_char = None
        temp = ""
        max_length = 0
        result = ""
        for char in input_string:
            if char != curr_char:
                curr_char = char
            elif char == curr_char:
                result += char

        return result


# Linked Lists: Implement a doubly linked list of integers class. Write a reverse method for your list class
# that reverses a list without changing the node contents.
class DoublyLinkedList(object):
    """docstring for DoublyLinkedList"""
    def __init__(self, arg):
        self.arg = arg
        
def reverse_doubly_linked_list(linked_list):
    pass

# Stacks and Queues: Write a program to evaluate arithmetical expressions that use + and applied
# to nonnegative integer arguments. Expressions are in reverse-Polish notation, e.g., 3 4 + 5 , 1 3 + 5 7 + *.
def evaluate_reverse_polish(expression):
    pass

# Binary Trees: Write inorder, preorder and postorder traversal methods for a binary tree. (You will need
#         to implement a class suitable for representing binary trees, but do not need to implement
#         add, lookup, delete, etc. methods.)
class BinaryTree(object):
    """docstring for BinaryTreeNode"""
    def __init__(self, arg):
        self.arg = arg
        

def inorder_traversal(bt):
    pass


def preorder_traversal(bt):
    pass


def postorder_traversal(bt):
    pass

# Heaps: Write a program that builds a max-heap from an integer array. (You will need to implement
#         a class suitable for representing heaps, but do not need to implement extract-max, insert key, etc.)

class Heap(object):
    """docstring for Heap"""
    def __init__(self, arg):
        self.arg = arg
        
def construct_max_heap(int_arr):
    pass

# Searching: Write a nonrecursive program to perform binary search over a sorted array.
def nonrecursive_binary_search(sorted_arr):
    pass

# Hash tables: Write a program that finds the most common object in an array of objects. The
# objects consists of pairs of strings. Treat strings as being the same if they are equal when converted to lower case.
def find_most_common_obj(object_arr):
    pass

# BSTs: Write a program that searches a BST on integer keys for a given value. (You will need to
#         implement a class suitable for representing BSTs, but do not need to implement
#         add, lookup, delete, etc. methods.)
class BinarySearchTree(object):
    """docstring for BinarySearchTree"""
    def __init__(self, arg):
        self.arg = arg

    def search(self, val_to_find):
        pass



# Write a recursive program that takes as input positive integers x and N, and returns x to the power N.
# You should use O(log N) multiplications.
def recursive_exponentiation(x, N):
    pass

# Dynamic Programming: Write a program that takes a positive integer N, and returns the number
# of binary strings of length N such that there are no consecutive 1s. For example, if N = 3, the result
# is 5, corresponding to the strings 000, 001, 010, 100, 101.


# Greedy Algorithms and Invariants: Write a program that takes an input a positive integer
# N, and returns the minimum number of coins in the US coinage system to create N cents. For example, if
# N = 37, the answer is 4, corresponding to a quarter, a dime, and two pennies.


# Graphs: Implement Depth First Search and Breadth First Search. (You will need to implement
#         classes suitable to representing graphs.)


# Parallel Computing: Write a program which uses two threads to print the numbers from
# 1 to 100 in order. One thread can only print odd numbers, the other can only print even numbers.

