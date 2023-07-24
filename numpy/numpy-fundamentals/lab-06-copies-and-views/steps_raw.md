# NumPy Basics Lab

## Introduction

In this lab, you will learn the basics of working with NumPy arrays. NumPy is a powerful library for numerical computing in Python. It provides efficient data structures and functions for performing mathematical operations on arrays.

## Steps

### Step 1: Understanding Copies and Views

NumPy arrays consist of two parts: the data buffer and the metadata. The data buffer contains the actual data elements, while the metadata includes information such as data type and strides.

When operating on NumPy arrays, it is important to understand the difference between copies and views:

- A **view** allows you to access the array differently by changing certain metadata without changing the data buffer. Any changes made to a view will be reflected in the original array.

- A **copy** is a new array that duplicates both the data buffer and the metadata. Changes made to a copy will not affect the original array.

### Step 2: Creating Views

Views can be created by changing certain metadata of an array. This creates a new way of looking at the data without copying it. To create a view, you can use the `view()` method of the `ndarray` object.

```python
import numpy as np

# Create an array
x = np.array([1, 2, 3, 4, 5])

# Create a view
y = x.view()

# Modify the view
y[0] = 10

# Print the original array
print(x)  # Output: [10, 2, 3, 4, 5]
```

In the above example, the view `y` allows us to modify the original array `x`.

### Step 3: Creating Copies

Copies can be created by duplicating both the data buffer and the metadata of an array. To create a copy, you can use the `copy()` method of the `ndarray` object.

```python
import numpy as np

# Create an array
x = np.array([1, 2, 3, 4, 5])

# Create a copy
y = x.copy()

# Modify the copy
y[0] = 10

# Print the original array
print(x)  # Output: [1, 2, 3, 4, 5]
```

In the above example, the copy `y` is independent of the original array `x`.

### Step 4: Indexing Operations

Indexing operations in NumPy can either create views or copies, depending on the type of indexing.

- Basic indexing always creates views. For example:

```python
import numpy as np

# Create an array
x = np.arange(10)

# Create a view
y = x[1:3]

# Modify the view
y[0] = 10

# Print the original array
print(x)  # Output: [0, 10, 2, 3, 4, 5, 6, 7, 8, 9]
```

In the above example, the view `y` reflects the changes made to the original array `x`.

- Advanced indexing always creates copies. For example:

```python
import numpy as np

# Create an array
x = np.arange(9).reshape(3, 3)

# Create a copy
y = x[[1, 2]]

# Modify the original array
x[[1, 2]] = [[10, 11, 12], [13, 14, 15]]

# Print the copy
print(y)  # Output: [[3, 4, 5], [6, 7, 8]]
```

In the above example, the copy `y` remains unchanged after modifying the original array `x`.

### Step 5: Other Operations

There are other operations in NumPy that can create views or copies.

- The `reshape()` function creates a view where possible or a copy otherwise. For example:

```python
import numpy as np

# Create an array
x = np.ones((2, 3))

# Transpose the array
y = x.T

# Attempt to reshape the array
try:
    y.shape = 6
except AttributeError:
    print("Incompatible shape for in-place modification. Use `.reshape()` to make a copy with the desired shape.")
```

In the above example, the array `y` becomes non-contiguous after transposing, so reshaping it requires a copy.

- The `ravel()` function returns a contiguous flattened view of the array wherever possible. On the other hand, the `flatten()` method always returns a flattened copy of the array. For example:

```python
import numpy as np

# Create an array
x = np.arange(9).reshape(3, 3)

# Create a flattened view
y = x.ravel()

# Create a flattened copy
z = x.flatten()

# Print the original array
print(x)  # Output: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

In the above example, `y` is a view, while `z` is a copy.

### Step 6: Determining if an Array is a View or a Copy

You can use the `base` attribute of the `ndarray` object to determine if an array is a view or a copy. The `base` attribute returns the original array for a view and `None` for a copy. For example:

```python
import numpy as np

# Create an array
x = np.arange(9)

# Create a view
y = x.reshape(3, 3)

# Create a copy
z = y[[2, 1]]

# Check if y is a view
print(y.base)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Check if z is a copy
print(z.base is None)  # Output: True
```

In the above example, `y` is a view and `z` is a copy.

## Summary

In this lab, you learned the basics of working with NumPy arrays. You learned about copies and views, and how to create them. You also learned about indexing operations and other operations that can create views or copies. Finally, you learned how to determine if an array is a view or a copy using the `base` attribute.

By understanding these concepts and using the appropriate methods, you can efficiently manipulate and analyze data using NumPy.
