# Data Reshaping with Pandas

## Introduction

In data analysis, it is common to encounter datasets that are not arranged in the way we want. Reshaping data refers to the process of changing how data is organized into rows and columns. In this lab, we will explore some of the key methods in Pandas for reshaping data including Pivot, Stack, Unstack, Melt, Cross tabulations, Tiling, Factorizing, and Exploding.

## Steps

### Step 1: Importing Necessary Libraries and Create DataFrame

First, let's import the necessary libraries and create a DataFrame for our examples.

```python
import pandas as pd
import numpy as np

# Create DataFrame
np.random.seed([3, 1415])
n = 20
cols = np.array(["key", "row", "item", "col"])
df = cols + pd.DataFrame((np.random.randint(5, size=(n, 4)) // [2, 1, 2, 1]).astype(str))
df.columns = cols
df = df.join(pd.DataFrame(np.random.rand(n, 2).round(2)).add_prefix("val"))
```

### Step 2: Pivoting with Single Aggregations

Pivot is one of the key methods for reshaping data in Pandas. It provides a way to transform your data so that you can view it from different angles.

```python
# Pivot df with the mean of val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc="mean", fill_value=0)
```

### Step 3: Pivoting with Multiple Aggregations

We can also perform multiple aggregations in Pivot.

```python
# Pivot df with the mean and sum of val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc=["mean", "sum"])
```

### Step 4: Cross Tabulations

Cross tabulation is a method to quantitatively analyze the relationship between multiple variables.

```python
# Cross tabulation between row and col
df.pivot_table(index="row", columns="col", fill_value=0, aggfunc="size")
```

### Step 5:
