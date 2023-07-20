# Working with Columns in Pandas

## Introduction

In this lab, we will learn how to work with columns in Pandas. We will explore how to create new columns derived from existing ones, apply mathematical and logical operations on columns, rename column labels, and perform column-wise operations using the `apply` method.

## Steps

### Step 1: Import Pandas and Load Data

First, we'll import the pandas library and load the air quality data from a CSV file.

```python
# Import pandas library
import pandas as pd

# Load air quality data
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
```

### Step 2: Create a New Column

We'll create a new column, "london_mg_per_cubic", by multiplying the "station_london" column by a conversion factor.

```python
# Create new column by multiplying "station_london" by conversion factor
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
```

### Step 3: Check the Ratio of Values in Two Columns

Next, we'll check the ratio of the values in the "station_paris" and "station_antwerp" columns and save the result in a new column.

```python
# Create new column by dividing "station_paris" by "station_antwerp"
air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]
```

### Step 4: Rename Column Labels

We'll rename the column labels to match the station identifiers used by OpenAQ.

```python
# Rename column labels
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
```

### Step 5: Convert Column Labels to Lowercase

Finally, we'll convert the column labels to lowercase using a function.

```python
# Convert column labels to lowercase
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
```

## Summary

In this lab, we learned how to create new columns derived from existing ones, perform mathematical and logical operations on columns, rename column labels, and convert column labels to lowercase. With these skills, we can manipulate and transform data in pandas more effectively.
