# Introduction to Indexing in NumPy

## Introduction

In this lab, we will explore the basics of indexing in NumPy. Indexing allows us to access and manipulate specific elements or subsets of elements in an array. Understanding how to use indexing effectively is crucial for working with arrays in NumPy.

## Steps

### Step 1: Import NumPy

First, let's import the NumPy library so that we can use its functions and data types.

```python
import numpy as np
```

### Step 2: Basic Indexing

NumPy arrays can be indexed using the standard Python syntax `x[obj]`, where `x` is the array and `obj` is the selection. There are different kinds of indexing available depending on the type of `obj`.

#### Single Element Indexing

Single element indexing works exactly like indexing for other standard Python sequences. It is 0-based and accepts negative indices for indexing from the end of the array.

```python
x = np.arange(10)
print(x[2])  # Output: 2
print(x[-2])  # Output: 8
```

#### Multidimensional Indexing

Arrays can have multiple dimensions, and indexing works the same way for each dimension. You can access elements in a multidimensional array by separating each dimension's index with a comma.

```python
x = np.arange(10).reshape(2, 5)
print(x[1, 3])  # Output: 8
print(x[1, -1])  # Output: 9
```

#### Subdimensional Array Indexing

If you index a multidimensional array with fewer indices than dimensions, you get a subdimensional array. Each index specified selects the array corresponding to the rest of the dimensions selected.

```python
x = np.arange(10).reshape(2, 5)
print(x[0])  # Output: [0, 1, 2, 3, 4]
```

### Step 3: Slicing and Striding

Basic slicing in NumPy extends Python's slicing concept to N dimensions. It allows you to select a range of elements along each dimension of an array.

#### Basic Slicing

Basic slicing occurs when `obj` is a slice object (constructed by `start:stop:step` notation inside of brackets), an integer, or a tuple of slice objects and integers.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[1:7:2])  # Output: [1, 3, 5]
```

#### Negative Indices

Negative indices can be used to index from the end of the array. For example, `-1` refers to the last element, `-2` refers to the second-to-last element, and so on.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[-2:10])  # Output: [8, 9]
print(x[-3:3:-1])  # Output: [7, 6, 5, 4]
```

#### Default Values for Slicing

If the start index is not specified, it defaults to 0 for positive step values and `-n-1` for negative step values. If the stop index is not specified, it defaults to `n` for positive step values and `-n-1` for negative step values. If the step is not specified, it defaults to 1.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[5:])  # Output: [5, 6, 7, 8, 9]
```

### Step 4: Advanced Indexing

Advanced indexing is triggered when the selection object `obj` is a non-tuple sequence object, an ndarray (of data type integer or bool), or a tuple with at least one sequence object or ndarray (of data type integer or bool). There are two types of advanced indexing: integer and boolean.

#### Integer Array Indexing

Integer array indexing allows selection of arbitrary items in the array based on their N-dimensional index. Each integer array represents a number of indices into that dimension.

```python
x = np.arange(10, 1, -1)
print(x[np.array([3, 3, 1, 8])])  # Output: [7, 7, 9, 2]
print(x[np.array([3, 3, -3, 8])])  # Output: [7, 7, 4, 2]
```

#### Boolean Array Indexing

Boolean array indexing allows selection of array elements based on a boolean condition. The result is a new array that contains only the elements corresponding to the `True` values of the boolean array.

```python
x = np.array([1., -1., -2., 3])
x[x < 0] += 20
print(x)  # Output: [ 1., 19., 18., 3.]
```

### Step 5: Field Access

If the ndarray object is a structured array, the fields of the array can be accessed by indexing the array with strings, dictionary-like.

```python
x = np.array([(1, 2), (3, 4), (5, 6)], dtype=[('a', np.int32), ('b', np.int32)])
print(x['a'])  # Output: [1, 3, 5]
```

### Step 6: Flat Iterator Indexing

The `x.flat` attribute returns an iterator that can be used to iterate over the entire array in C-contiguous style. This iterator can also be indexed using basic slicing or advanced indexing.

```python
x = np.arange(10)
iterator = x.flat
print(iterator[1:5])  # Output: [1, 2, 3, 4]
```

### Step 7: Assigning Values to Indexed Arrays

You can assign values to specific elements or subsets of elements in an array using indexing. The value being assigned must be shape consistent with the indexed array.

```python
x = np.arange(10)
x[2:7] = 1
print(x)  # Output: [0, 1, 1, 1, 1, 1, 7, 8, 9]

x = np.arange(10)
x[2:7] = np.arange(5)
print(x)  # Output: [0, 1, 0, 1, 2, 3, 7, 8, 9]
```

## Summary

In this lab, we explored the basics of indexing in NumPy. We learned how to use basic indexing, slicing, advanced indexing, field access, flat iterator indexing, and assigning values to indexed arrays. Understanding these indexing techniques is essential for working with arrays effectively in NumPy.
