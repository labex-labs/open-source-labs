# Search Sorted Matrix

## Problem

Given a sorted matrix, we need to search for a specific item in it. The matrix is sorted in such a way that the items in each row and column are sorted in ascending order. The matrix is not necessarily a square matrix. We need to return the position of the item in the matrix as a tuple (row, col) if it is found, otherwise, we need to return None.

## Requirements

To solve this problem, we need to make the following assumptions:

- The items in each row of the matrix are sorted in ascending order.
- The items in each column of the matrix are sorted in ascending order.
- The matrix is not jagged, i.e., it is a rectangle.
- The sorting order is ascending.
- The matrix is not necessarily a square matrix.
- The output is a tuple (row, col).
- The item we are searching for may or may not be in the matrix.
- The inputs may or may not be valid.
- The solution should fit in memory.

## Example Usage

We can use the following test cases to verify our solution:

- If the input is None, the function should raise an exception.
- If the item is found in the matrix, the function should return its position as a tuple (row, col).
- If the item is not found in the matrix, the function should return None.
