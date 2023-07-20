# Introduction to Pandas

## Introduction

In this lab, we will introduce you to the basics of pandas, a powerful data manipulation library in Python. We will guide you through various tasks such as importing pandas, creating and viewing data, data selection, operations and much more.

## Steps

### Step 1: Importing Pandas and Numpy

First, we need to import pandas and numpy packages. Pandas is a powerful data manipulation library and numpy is used for mathematical operations.

```python
# Importing necessary libraries
import numpy as np
import pandas as pd
```

### Step 2: Creating Objects

We will create a `Series` by passing a list of values, and pandas will create a default integer index.

```python
# Creating a pandas series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s
```

### Step 3: Creating Dataframes

We can create a `DataFrame` by passing a numpy array, with a datetime index and labeled columns.

```python
# Creating a pandas dataframe
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df
```

### Step 4: Viewing Data

We can view the top and bottom rows of the dataframe using `head()` and `tail()` methods respectively.

```python
# Viewing top rows
df.head()

# Viewing bottom rows
df.tail(3)
```

### Step 5: Data Selection

We can select data using labels or by position.

```python
# Selecting a single column
df["A"]

# Selecting via position
df.iloc[3]
```

### Step 6: Data Operations

We can perform operations on dataframes like sorting, applying functions, etc.

```python
# Sorting by an axis
df.sort_index(axis=1, ascending=False)

# Applying a function to the data
df.apply(np.cumsum)
```

### Step 7: Handling Missing Data

Pandas provides methods to handle missing data in the dataframe.

```python
# Filling missing data
df1.fillna(value=5)

# Getting the boolean mask where values are nan
pd.isna(df1)
```

### Step 8: Plotting Data

Pandas uses matplotlib for plotting data.

```python
# Plotting data
df.plot()
```

### Step 9: Saving and Loading Data

Pandas provides methods to save and load data in various formats like csv, excel, hdf5, etc.

```python
# Saving data to a csv file
df.to_csv("foo.csv")

# Loading data from a csv file
pd.read_csv("foo.csv")
```

## Summary

In this lab, we covered the basics of pandas, including how to create and view data, how to select and manipulate data, and how to save and load data. We also learned how to handle missing data and how to plot data. This should provide a solid foundation for further exploration of pandas for data analysis.
