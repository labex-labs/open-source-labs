# Introduction to NumPy Universal Functions

## Introduction

In this lab, we will explore the basics of NumPy Universal Functions (ufuncs). Ufuncs are functions that operate on ndarrays in an element-by-element fashion, supporting array broadcasting, type casting, and other standard features. We will learn about the different methods of ufuncs, broadcasting rules, type casting rules, and how to override ufunc behavior.

## Steps

### Step 1: Basic Arithmetic Operations

The basic ufuncs operate on scalars, and the simplest example is the addition operator. Let's see how we can use the addition operator to add two arrays element-wise.

```python
import numpy as np

# Create two arrays
arr1 = np.array([0, 2, 3, 4])
arr2 = np.array([1, 1, -1, 2])

# Add the arrays element-wise
result = arr1 + arr2

# Print the result
print(result)
```

Output:

```
array([1, 3, 2, 6])
```

### Step 2: Ufunc Methods

Ufuncs have four methods: reduce, accumulate, reduceat, and outer. These methods are useful for performing operations on arrays. Let's take a look at the reduce method.

```python
import numpy as np

# Create an array
arr = np.arange(9).reshape(3, 3)

# Reduce the array along the first axis
result = np.add.reduce(arr, 1)

# Print the result
print(result)
```

Output:

```
array([ 3, 12, 21])
```

### Step 3: Output Type Determination

The output of a ufunc is not necessarily an ndarray if all input arguments are not ndarrays. The output type can be determined based on the input types and the rules of type casting. Let's see an example.

```python
import numpy as np

# Create an array
arr = np.arange(9).reshape(3, 3)

# Perform multiplication and specify the output type
result = np.multiply.reduce(arr, dtype=float)

# Print the result
print(result)
```

Output:

```
array([ 0., 28., 80.])
```

### Step 4: Broadcasting

Broadcasting is a powerful feature of ufuncs that allows operations to be performed on arrays with different shapes. The broadcasting rules determine how arrays with different shapes are treated during operations. Let's see an example.

```python
import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1], [2], [3]])

# Multiply the arrays
result = arr1 * arr2

# Print the result
print(result)
```

Output:

```
array([[1, 2, 3],
       [2, 4, 6],
       [3, 6, 9]])
```

### Step 5: Type Casting Rules

Type casting is done on the inputs of a ufunc when there is no core loop implementation for the input types provided. The casting rules determine when a data type can be safely cast to another data type. Let's see an example.

```python
import numpy as np

# Check if int can be safely cast to float
result = np.can_cast(np.int, np.float)

# Print the result
print(result)
```

Output:

```
True
```

### Step 6: Overriding Ufunc Behavior

Classes, including ndarray subclasses, can override how ufuncs act on them by defining certain special methods. This allows for customization of ufunc behavior. Let's see an example.

```python
import numpy as np

# Define a custom class
class MyArray(np.ndarray):
    def __add__(self, other):
        print("Custom add method called")
        return super().__add__(other)

# Create an instance of the custom class
arr = MyArray([1, 2, 3])

# Perform addition
result = arr + 1

# Print the result
print(result)
```

Output:

```
Custom add method called
[2 3 4]
```

## Summary:

In this lab, we learned about the basics of NumPy Universal Functions (ufuncs). We explored the different methods of ufuncs, broadcasting rules, type casting rules, and how to override ufunc behavior. Ufuncs are a powerful tool for performing element-wise operations on arrays efficiently.
