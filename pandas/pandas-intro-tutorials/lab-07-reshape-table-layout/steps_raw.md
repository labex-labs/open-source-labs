# Reshaping Data with Pandas

## Introduction

In this lab, we will explore how to reshape data in pandas using various functions like `sort_values`, `pivot`, `pivot_table`, and `melt`. We will work with the Titanic and Air Quality datasets to demonstrate the reshaping techniques.

## Steps

### Step 1: Import Libraries and Load Data

First, let's import the required libraries and load the datasets.

```python
import pandas as pd

# Load Titanic dataset
titanic = pd.read_csv("data/titanic.csv")

# Load Air Quality dataset
air_quality = pd.read_csv("data/air_quality_long.csv", index_col="date.utc", parse_dates=True)
```

### Step 2: Sort Table Rows

Sort the Titanic dataset according to the age of the passengers and then by cabin class and age in descending order.

```python
# Sort by Age
titanic.sort_values(by="Age").head()

# Sort by Pclass and Age in descending order
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()
```

### Step 3: Convert Long to Wide Table Format

We will now convert the long format data of air quality to wide format using the `pivot` function.

```python
# Filter for no2 data only
no2 = air_quality[air_quality["parameter"] == "no2"]

# Use 2 measurements (head) for each location (groupby)
no2_subset = no2.sort_index().groupby(["location"]).head(2)

# Pivot the data
no2_subset.pivot(columns="location", values="value")
```

### Step 4: Create a Pivot Table

Create a pivot table to find the mean concentrations for 𝑁𝑂2 and 𝑃𝑀25 in each of the stations.

```python
air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
```

### Step 5: Convert Wide to Long Format

Now, let's convert the wide format data of 𝑁𝑂2 to long format using the `melt` function.

```python
# Reset index for no2_pivoted
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

# Melt the data
no_2 = no2_pivoted.melt(id_vars="date.utc")
```

## Summary

In this lab, we learned how to reshape data in pandas using various functions like `sort_values`, `pivot`, `pivot_table`, and `melt`. We applied these techniques on the Titanic and Air Quality datasets to sort, pivot, and melt the data. These reshaping techniques are essential when working with data in pandas and can help us to efficiently analyze and visualize the data.
