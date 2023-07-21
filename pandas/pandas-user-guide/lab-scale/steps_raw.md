# Scaling Large Datasets

## Introduction

This lab focuses on how to scale data analysis to larger datasets using pandas. It covers methods like loading less data, using efficient data types, chunking, and leveraging other libraries like Dask. It is important to note that pandas is more suited for in-memory analytics and might not be the best tool for very large datasets.

## Steps

### Step 1: Generate Dataset

The first step is to generate a large dataset for testing. We create a dataset with many columns that can be stored in a parquet file. This step requires pandas and numpy libraries.

```python
import pandas as pd
import numpy as np

def make_timeseries(start="2000-01-01", end="2000-12-31", freq="1D", seed=None):
    # Function to generate timeseries data
    index = pd.date_range(start=start, end=end, freq=freq, name="timestamp")
    n = len(index)
    state = np.random.RandomState(seed)
    columns = {
        "name": state.choice(["Alice", "Bob", "Charlie"], size=n),
        "id": state.poisson(1000, size=n),
        "x": state.rand(n) * 2 - 1,
        "y": state.rand(n) * 2 - 1,
    }
    df = pd.DataFrame(columns, index=index, columns=sorted(columns))
    if df.index[-1] == end:
        df = df.iloc[:-1]
    return df

timeseries = [
    make_timeseries(freq="1T", seed=i).rename(columns=lambda x: f"{x}_{i}")
    for i in range(10)
]
ts_wide = pd.concat(timeseries, axis=1)
ts_wide.to_parquet("timeseries_wide.parquet")
```

### Step 2: Load Less Data

Instead of loading all the data, we can load only the columns we need. Here, we demonstrate two methods to load less data from the parquet file.

```python
# Option 1: Load all data then filter
columns = ["id_0", "name_0", "x_0", "y_0"]
pd.read_parquet("timeseries_wide.parquet")[columns]

# Option 2: Load only the requested columns
pd.read_parquet("timeseries_wide.parquet", columns=columns)
```

### Step 3: Use Efficient Datatypes

Pandas' default data types are not the most memory efficient. This step shows how to use more efficient data types to store larger datasets in memory.

```python
ts = make_timeseries(freq="30S", seed=0)
ts.to_parquet("timeseries.parquet")
ts = pd.read_parquet("timeseries.parquet")

# Convert 'name' column to 'category' type for efficiency
ts2 = ts.copy()
ts2["name"] = ts2["name"].astype("category")

# Downcast numeric columns to their smallest types
ts2["id"] = pd.to_numeric(ts2["id"], downcast="unsigned")
ts2[["x", "y"]] = ts2[["x", "y"]].apply(pd.to_numeric, downcast="float")
```

### Step 4: Use Chunking

Chunking is a method to split a large problem into smaller problems that can be solved independently. As long as each chunk fits in memory, you can work with datasets that are much larger than memory.

```python
files = pathlib.Path("data/timeseries/").glob("ts*.parquet")
counts = pd.Series(dtype=int)
for path in files:
    df = pd.read_parquet(path)
    counts = counts.add(df["name"].value_counts(), fill_value=0)
counts.astype(int)
```

### Step 5: Use Other Libraries

Other libraries like Dask can handle larger-than-memory datasets. Dask provides a pandas-like API and can process data in parallel.

```python
import dask.dataframe as dd

ddf = dd.read_parquet("data/timeseries/ts*.parquet", engine="pyarrow")

# Compute value counts using Dask
ddf["name"].value_counts().compute()
```

## Summary

In this lab, we demonstrated different techniques for scaling data analysis to larger datasets using pandas. We generated a large dataset, learned how to load less data, use efficient datatypes, and chunking. We also explored how to leverage other libraries like Dask for handling larger-than-memory datasets. The techniques and concepts learned in this lab will be useful when dealing with large datasets in data analysis projects.
