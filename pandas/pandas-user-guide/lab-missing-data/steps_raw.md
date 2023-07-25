# Handling Missing Data

## Introduction

In this lab, we will learn how to handle missing data in pandas, a common issue in data analysis. We'll cover how to identify missing data, fill in missing values, and drop data that's not needed. We will also discuss the experimental `NA` scalar in pandas that can be used to denote missing values.

## Steps

### Step 1: Import Necessary Libraries and Create DataFrame

To start, we need to import the necessary libraries - pandas and NumPy. Then, we'll create a DataFrame with some missing values.

```python
import pandas as pd
import numpy as np

# Create a DataFrame with missing values
df = pd.DataFrame(
   np.random.randn(5, 3),
   index=["a", "c", "e", "f", "h"],
   columns=["one", "two", "three"],
)
df["four"] = "bar"
df["five"] = df["one"] > 0
df2 = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])
```

### Step 2: Detect Missing Values

Next, we'll use the `isna` and `notna` functions to detect missing values.

```python
# Use isna and notna to detect missing values
pd.isna(df2["one"])
df2["four"].notna()
df2.isna()
```

### Step 3: Insert Missing Data

Here, we'll see how to insert missing values into our data.

```python
# Insert missing values
s = pd.Series([1., 2., 3.])
s.loc[0] = None
```

### Step 4: Perform Calculations with Missing Data

We'll perform some basic arithmetic and statistical calculations with missing data.

```python
# Perform calculations with missing data
df["one"].sum()
df.mean(1)
df.cumsum()
```

### Step 5: Drop Axis Labels with Missing Data

We'll learn how to exclude labels with missing data using `dropna`.

```python
df.dropna(axis=0)
df.dropna(axis=1)
df["one"].dropna()
```

### Step 6: Interpolate Missing Values

We'll use the `interpolate` function to fill in missing values in a DataFrame.

```python
df = pd.DataFrame(
   {
       "A": [1, 2.1, np.nan, 4.7, 5.6, 6.8],
       "B": [0.25, np.nan, np.nan, 4, 12.2, 14.4],
   }
)
df.interpolate()
```

### Step 7: Replace Generic Values

We'll learn how to replace arbitrary values with other values using `replace`.

```python
ser = pd.Series([0.0, 1.0, 2.0, 3.0, 4.0])
ser.replace(0, 5)
```

### Step 8: Understand NA Scalar to Denote Missing Values

Finally, we'll discuss the experimental `NA` scalar in pandas that can be used to denote missing values.

```python
s = pd.Series([1, 2, None], dtype="Int64")
s
```

## Summary

In this lab, we have learned how to handle missing data using pandas. We have covered how to detect, insert, calculate with, and drop missing data. We have also learned how to interpolate and replace missing values. Lastly, we have discussed the experimental `NA` scalar in pandas to denote missing values. This knowledge will be very useful when dealing with real-world data analysis tasks where missing data is often a common issue.
