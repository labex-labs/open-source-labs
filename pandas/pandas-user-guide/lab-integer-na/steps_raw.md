# Working with Nullable Integers

## Introduction

In this lab, we will explore how to use the nullable integer data type in pandas, which is an efficient way to handle integer data that may contain missing values. We will learn how to construct arrays with this data type, perform operations, and handle missing values effectively.

## Steps

### Step 1: Constructing Nullable Integer Arrays

Pandas provides the `IntegerArray` class for creating arrays of nullable integers. Let's start by creating an `IntegerArray`.

```python
# Import necessary libraries
import pandas as pd
import numpy as np

# Create an IntegerArray with missing values
arr = pd.array([1, 2, None], dtype=pd.Int64Dtype())
# Output: <IntegerArray>
# [1, 2, <NA>]
# Length: 3, dtype: Int64
```

You can also use the string alias "Int64" to specify the data type when creating the array. All NA-like values are replaced with `pandas.NA`.

```python
# Create an IntegerArray using the "Int64" string alias
arr = pd.array([1, 2, np.nan], dtype="Int64")
# Output: <IntegerArray>
# [1, 2, <NA>]
# Length: 3, dtype: Int64
```

### Step 2: Storing the IntegerArray in a DataFrame or Series

Once you have created an `IntegerArray`, you can store it in a `DataFrame` or `Series`. Let's create a `Series` from the `IntegerArray` we created.

```python
# Create a Series from the IntegerArray
series = pd.Series(arr)
```

### Step 3: Performing Operations with Nullable Integer Arrays

You can perform various operations with nullable integer arrays, such as arithmetic operations, comparisons, and slicing.

```python
# Create a Series with nullable integer type
s = pd.Series([1, 2, None], dtype="Int64")

# Perform arithmetic operation
s_plus_one = s + 1 # adds 1 to each element in the series

# Perform comparison
comparison = s == 1 # checks if each element in the series is equal to 1

# Perform slicing operation
sliced = s.iloc[1:3] # selects the second and third elements in the series
```

### Step 4: Handling Missing Values with pandas.NA

The `IntegerArray` class uses `pandas.NA` as its scalar missing value. When you slice a single element that's missing, it will return `pandas.NA`.

```python
# Create an IntegerArray with a missing value
a = pd.array([1, None], dtype="Int64")

# Slice the second element which is a missing value
missing_value = a[1]
# Output: <NA>
```

## Summary

This lab demonstrated how to work with nullable integer data types in pandas, including how to construct arrays, store them in a `DataFrame` or `Series`, perform operations, and handle missing values. By using the nullable integer data type, you can handle integer data with missing values more efficiently.
