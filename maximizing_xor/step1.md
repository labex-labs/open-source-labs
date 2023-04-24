# Maximizing Xor

## Problem

Given two integers, L and R, find the maximum value of A xor B, where A and B satisfy the following condition:

L ≤ A ≤ B ≤ R

For example, if L=10 and R=15, then the pairs that satisfy the condition are (10,10), (10,11), (10,12), (10,13), (10,14), (10,15), (11,11), (11,12), (11,13), (11,14), (11,15), (12,12), (12,13), (12,14), (12,15), (13,13), (13,14), (13,15), (14,14), (14,15), and (15,15). The maximum value of A xor B is 7, which is obtained when (10,15) are chosen.

## Requirements

To solve this problem, you will need to use the following:

- Basic knowledge of Python programming language
- Bitwise operators in Python
- Loops and conditional statements in Python

## Example Usage

```python
def maximizingXor(l, r):
    max_xor = 0
    for i in range(l, r+1):
        for j in range(i, r+1):
            xor = i ^ j
            if xor > max_xor:
                max_xor = xor
    return max_xor

print(maximizingXor(10, 15)) # Output: 7
```
