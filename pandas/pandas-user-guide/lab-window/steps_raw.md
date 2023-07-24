# Windowing Operations in Pandas

## Introduction

In this lab, we will explore the windowing operations in pandas, including rolling windows, expanding windows, and exponentially weighted windows. Windowing operations are useful for performing aggregations over a sliding partition of values.

## Steps

### Step 1: Create a Pandas Series

We create a pandas series with a range of values from 0 to 4.

```python
import pandas as pd

# Create a pandas series with a range of values from 0 to 4
s = pd.Series(range(5))
```

### Step 2: Perform Rolling Window Operation

Perform a rolling window operation with a window size of 2 and then calculate the sum for each window.

```python
# Perform a rolling window operation with a window size of 2 and calculate the sum for each window
s.rolling(window=2).sum()
```

### Step 3: Perform Expanding Window Operation

Perform an expanding window operation and then calculate the sum for each window.

```python
# Perform an expanding window operation and calculate the sum for each window
s.expanding(min_periods=1).sum()
```

### Step 4: Perform Exponentially Weighted Window Operation

Perform an exponentially weighted window operation and then calculate the mean for each window.

```python
# Perform an exponentially weighted window operation and calculate the mean for each window
s.ewm(span=3).mean()
```

## Summary

In this lab, we performed various windowing operations using pandas, including rolling windows, expanding windows, and exponentially weighted windows. These operations are useful for performing aggregations over a sliding partition of values.
