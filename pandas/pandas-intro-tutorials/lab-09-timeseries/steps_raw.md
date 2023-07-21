# Handling Time Series Data

## Introduction

This lab will guide you through handling time series data using the Python package, Pandas. We will be working with air quality data for this tutorial. You will learn how to convert strings into datetime objects, perform operations on these datetime objects, resample time series to another frequency, and more.

## Steps

### Step 1: Import the necessary libraries and load the data

First, we need to import the required Python libraries and load the air quality data. The data will be read into a pandas DataFrame, which is a 2-dimensional labeled data structure.

```python
# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# load the air quality data
air_quality = pd.read_csv("data/air_quality_no2_long.csv")

# rename the "date.utc" column to "datetime"
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
```

### Step 2: Convert strings to datetime objects

The dates in the "datetime" column are currently strings. We want to convert these to datetime objects for easier manipulation.

```python
# convert "datetime" column to datetime objects
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
```

### Step 3: Add a new column for the month of the measurement

Now, we want to add a new column to our DataFrame that contains only the month of each measurement. This can be achieved using the `dt` accessor.

```python
# add a new column for the month of each measurement
air_quality["month"] = air_quality["datetime"].dt.month
```

### Step 4: Calculate the average NO2 concentration for each day of the week

We can now calculate the average NO2 concentration for each day of the week at each measurement location. This can be done using the `groupby` method.

```python
# calculate the average NO2 concentration for each day of the week
average_NO2 = air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean()
```

### Step 5: Plot the average NO2 values for each hour of the day

We can also plot the average NO2 values for each hour of the day. This can be done using the `plot` method.

```python
# plot the average NO2 values for each hour of the day
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the day");
plt.ylabel("$NO_2 (µg/m^3)$");
```

### Step 6: Resample time series data

The `resample` method is a powerful way to change the frequency of time series data. Here, we will aggregate the current hourly time series data to the monthly maximum value at each measurement station.

```python
# resample time series data
monthly_max = air_quality.resample("M").max()
```

## Summary

In this lab, we learned how to handle time series data in Python using the pandas library. We loaded air quality data, converted date strings to datetime objects, calculated the average NO2 concentration for each day of the week, plotted the average NO2 values for each hour of the day, and resampled the time series data to a different frequency.
