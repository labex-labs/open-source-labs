# General Broadcasting Rules

NumPy compares the shapes of two arrays element-wise to determine if they are compatible for broadcasting. The following rules apply:

1. Two dimensions are compatible if they are equal in size.
2. Two dimensions are compatible if one of them has a size of 1.

If these conditions are not met, a `ValueError` is raised, indicating that the arrays have incompatible shapes.
