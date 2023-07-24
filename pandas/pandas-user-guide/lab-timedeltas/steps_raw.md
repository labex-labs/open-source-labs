# Working with Time Deltas

## Introduction

This lab guides you through the process of working with time deltas in Python using the pandas library. A time delta represents a duration or difference in time. We will explore different ways to construct, manipulate, and operate on time deltas.

## Steps

### Step 1: Import the Required Libraries

First, we need to import the necessary libraries. In this case, we will be using pandas and numpy.

```python
# Import the required libraries
import pandas as pd
import numpy as np
import datetime
```

### Step 2: Construct a Timedelta

Let's create a timedelta object, which represents a duration or difference in time.

```python
# Construct a timedelta object
pd.Timedelta("1 days 2 hours")
```

### Step 3: Convert to Timedelta

You can convert a scalar, array, list, or series from a recognized timedelta format into a timedelta type.

```python
# Convert a string to a timedelta
pd.to_timedelta("1 days 06:05:01.00003")
```

### Step 4: Perform Operations

You can perform mathematical operations on timedeltas.

```python
# Subtract two timedeltas
s = pd.Series(pd.date_range("2012-1-1", periods=3, freq="D"))
s - s.max()
```

### Step 5: Access Attributes

You can access various components of the timedelta directly.

```python
# Access the days attribute of a timedelta
tds = pd.Timedelta("31 days 5 min 3 sec")
tds.days
```

### Step 6: Convert to ISO 8601 Duration

You can convert a timedelta to an ISO 8601 Duration string.

```python
# Convert a timedelta to an ISO 8601 Duration string
pd.Timedelta(days=6, minutes=50, seconds=3, milliseconds=10, microseconds=10, nanoseconds=12).isoformat()
```

### Step 7: Create a Timedelta Index

You can generate an index with time deltas.

```python
# Generate a timedelta index
pd.TimedeltaIndex(["1 days", "1 days, 00:00:05", np.timedelta64(2, "D"), datetime.timedelta(days=2, seconds=2)])
```

### Step 8: Use the Timedelta Index

You can use the timedelta index as the index of pandas objects.

```python
# Use the timedelta index as the index of a pandas series
s = pd.Series(np.arange(100), index=pd.timedelta_range("1 days", periods=100, freq="h"))
```

### Step 9: Perform Operations with Timedelta Index

You can perform operations with the timedelta index.

```python
# Add a timedelta index to a datetime index
tdi = pd.TimedeltaIndex(["1 days", pd.NaT, "2 days"])
dti = pd.date_range("20130101", periods=3)
(dti + tdi).to_list()
```

### Step 10: Resample a Timedelta Index

You can resample data with a timedelta index.

```python
# Resample data with a timedelta index
s.resample("D").mean()
```

## Summary

In this lab, we learned how to work with time deltas in Python using the pandas library. We covered how to construct a timedelta, convert to timedelta, perform operations, access attributes, convert to ISO 8601 Duration, create a timedelta index, use the timedelta index, perform operations with timedelta index, and resample a timedelta index. With these skills, you can efficiently handle and manipulate time-based data in your future data analysis tasks.
