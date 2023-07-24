# Replicating, Joining, or Mutating Existing Arrays

Once you have created arrays, you can replicate, join, or mutate them to create new arrays. When assigning an array or its elements to a new variable, use the `np.copy` function to create a new array instead of a view into the original array. Here's an example:

```python
import numpy as np

# Create an array
a = np.array([1, 2, 3, 4])

# Create a view of the first two elements of the array
b = a[:2]

# Modify the view
b += 1

# Print the original array and the modified view
print('a =', a, '; b =', b)
```

To join arrays, you can use functions like `np.vstack`, `np.hstack`, and `np.block`. Here's an example of joining four 2-by-2 arrays into a 4-by-4 array using `np.block`:

```python
import numpy as np

A = np.ones((2, 2))
B = np.eye(2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))

result = np.block([[A, B], [C, D]])
```
