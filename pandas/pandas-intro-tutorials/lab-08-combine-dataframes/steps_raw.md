# Combining Data Tables in Pandas

## Introduction

In this lab, we will work with air quality data to explore how to combine multiple tables using Python's Pandas library. We will be using the `concat` and `merge` functions to perform these operations. This lab will help you understand how to concatenate and merge data frames effectively.

## Steps

### Step 1: Import Required Libraries

Our first step is to import the libraries we will need. For this lab, we will be using the pandas library.

```python
# Import the required library
import pandas as pd
```

### Step 2: Load the Datasets

We will load two datasets related to air quality. One contains Nitrate data and the other contains Particulate matter data.

```python
# Load the Nitrate data
air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv", parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]

# Load the Particulate matter data
air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv", parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]
```

### Step 3: Concatenating the Datasets

Next, we will combine the measurements of Nitrate and Particulate matter into a single table using the `concat` function.

```python
# Concatenate the two dataframes
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
```

### Step 4: Merge Tables Using a Common Identifier

We will then add the station coordinates to the measurements table using the `merge` function. We will perform a left join on the `location` column.

```python
# Load the stations coordinates data
stations_coord = pd.read_csv("data/air_quality_stations.csv")

# Merge the air_quality and stations_coord dataframes
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
```

### Step 5: Add Parameters' Full Description and Name

Lastly, we will add the parameters' full description and name to the measurements table. We perform a left join on the `parameter` and `id` columns.

```python
# Load the air quality parameters data
air_quality_parameters = pd.read_csv("data/air_quality_parameters.csv")

# Merge the air_quality and air_quality_parameters dataframes
air_quality = pd.merge(air_quality, air_quality_parameters, how='left', left_on='parameter', right_on='id')
```

## Summary

In this lab, we learned how to combine multiple tables in pandas. We used the `concat` function to concatenate tables and the `merge` function to join tables using a common identifier. These operations are crucial when working with multiple data sources that need to be combined into a single, coherent dataset for analysis.
