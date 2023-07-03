# Pandas Basics Lab

## Introduction

Welcome to the Pandas Basics Lab! In this lab, we will explore some fundamental aspects of the Pandas library: DataFrame memory usage, handling if/truth statements, using User Defined Function (UDF) methods, dealing with NA values, differences with NumPy, and thread-safety considerations.

## Steps

### Step 1: Understanding DataFrame Memory Usage

Pandas provides several methods to understand the memory usage of a DataFrame. The `.info()` method can be used to see a summary, including memory usage.

```python
import pandas as pd
import numpy as np

# Create a DataFrame
dtypes = ["int64", "float64", "datetime64[ns]", "timedelta64[ns]", "complex128", "object", "bool"]
n = 5000
data = {t: np.random.randint(100, size=n).astype(t) for t in dtypes}
df = pd.DataFrame(data)
df["categorical"] = df["object"].astype("category")

# Display DataFrame info
df.info()
```

### Step 2: Using if/truth Statements with Pandas

Pandas does not support using if/truth statements directly due to ambiguity. Instead, use methods like `.any()`, `.all()`, or `.empty()`.

```python
# Check if any value in the Series is True
if pd.Series([False, True, False]).any():
    print("At least one True value in the Series")
```

### Step 3: Mutating with User Defined Function (UDF) Methods

When using a pandas method that takes a UDF, avoid changing the DataFrame inside the UDF. Instead, make a copy before making changes.

```python
def f(s):
    s = s.copy()
    s.pop("a")
    return s

df = pd.DataFrame({"a": [1, 2, 3], 'b': [4, 5, 6]})
df.apply(f, axis="columns")
```

### Step 4: Dealing with NA Values

Pandas provides nullable-integer extension dtypes to represent integers with possibly missing values.

```python
s_int = pd.Series([1, 2, 3, 4, 5], index=list("abcde"), dtype=pd.Int64Dtype())
s2_int = s_int.reindex(["a", "b", "c", "f", "u"])
```

### Step 5: Understanding Differences with NumPy

Pandas and NumPy have slight differences in how they calculate variance. This is important to consider when switching between the two libraries.

```python
# Variance in pandas
var_pandas = df.var()

# Variance in NumPy
var_numpy = np.var(df.values)
```

### Step 6: Considering Thread-safety in Pandas

Pandas is not 100% thread safe. Be cautious when sharing pandas objects among multiple threads.

### Step 7: Handling Byte-ordering Issues

You may encounter byte-ordering issues when dealing with data created on a machine with a different byte order. Convert the data to the native system byte order before passing it to Pandas.

```python
x = np.array(list(range(10)), ">i4")  # big endian
newx = x.byteswap().newbyteorder()  # force native byteorder
s = pd.Series(newx)
```

## Summary

In this lab, we explored some crucial aspects of the Pandas library. Understanding these aspects will help you utilize Pandas more effectively and avoid common pitfalls.
