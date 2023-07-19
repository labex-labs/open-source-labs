# Working with Data Structures in Pandas

## Introduction

Pandas is a powerful Python library for data manipulation and analysis. Its fundamental data structures, Series and DataFrame, allow you to store and manipulate structured data. This lab will provide a step-by-step guide on how to work with these data structures, from creation to manipulation and alignment.

## Steps

### Step 1: Importing Necessary Libraries

Before we start, let's import the necessary libraries. We will need NumPy and pandas for this lab.

```python
# Import necessary libraries
import numpy as np
import pandas as pd
```

### Step 2: Creating a Series

The first data structure we will look at is a Series, which is a one-dimensional labeled array. It can hold any data type including integers, strings, floating point numbers, and Python objects.

```python
# Create a Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
```

### Step 3: Creating a DataFrame

The other fundamental data structure is the DataFrame. It's a two-dimensional labeled data structure with columns of potentially different types.

```python
# Create a DataFrame
df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
```

### Step 4: Manipulating DataFrame Columns

You can perform various operations on DataFrame columns. For example, you can select a column, add a new column, or delete a column.

```python
# Select column A
df['A']

# Add a new column E
df['E'] = pd.Series(np.random.randn(6), index=df.index)

# Delete column B
del df['B']
```

### Step 5: Data Alignment and Arithmetic

Data alignment is an important feature of pandas. When you perform operations on two objects, pandas aligns them by their associated labels.

```python
# Create two DataFrames
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])

# Perform addition operation
result = df1 + df2
```

### Step 6: Working with NumPy Functions

Most NumPy functions can be called directly on Series and DataFrame objects, providing a lot of flexibility for data manipulation and analysis.

```python
# Apply the exponential function to a DataFrame
np.exp(df)
```

## Summary

In this lab, we have learned about the two fundamental data structures in pandas: Series and DataFrame. We've seen how to create and manipulate these structures, and how to use NumPy functions directly on them. We also explored the concept of data alignment, which is a powerful feature of pandas that allows for intuitive data manipulation and analysis.
