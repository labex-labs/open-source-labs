# Matrix Mult

## Problem

Given a list of 2x2 matrices, we need to find the minimum cost of multiplying them together. The cost of multiplying two matrices is the number of scalar multiplications required. For example, if we have matrices A, B, and C, and we want to calculate the product ABC, the cost would be the number of scalar multiplications required to compute each element of the resulting matrix.

To solve this problem, we need to find the optimal order of multiplying the matrices. The order in which we multiply the matrices affects the total cost of the multiplication. For example, if we have matrices A, B, and C, and we want to calculate the product ABC, we can either compute (AB)C or A(BC). The cost of these two computations may be different, and we need to find the optimal order that minimizes the cost.

## Requirements

To solve this problem, we need to consider the following requirements:

- We only need to calculate the cost of matrix multiplication and not list the actual order of operations.
- We cannot assume that the inputs are valid and need to handle invalid inputs.
- We can assume that the problem fits memory.

## Example Usage

Here are some examples of how the function should behave:

- `None` -> `Exception`
- `[]` -> `0`
- `[Matrix(2, 3), Matrix(3, 6), Matrix(6, 4), Matrix(4, 5)]` -> `124`
