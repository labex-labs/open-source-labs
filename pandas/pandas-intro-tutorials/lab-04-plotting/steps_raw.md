# Pandas Plotting Tutorial

## Introduction

In this lab, we will learn how to create plots using Pandas, a powerful data manipulation library in Python. We will use real air quality data for practical illustrations. By the end of this lab, you should be able to use Pandas to create line plots, scatter plots, box plots, and customize your plots.

## Steps

### Step 1: Import Necessary Libraries

First, we need to import the necessary libraries. We will use Pandas for data manipulation and Matplotlib for data visualization.

```python
# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
```

### Step 2: Load the Data

We will use air quality data for this tutorial. The data will be loaded from a CSV file into a Pandas DataFrame.

```python
# Loading the data
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
air_quality.head()
```

### Step 3: Create a Line Plot

Pandas creates a line plot for each of the columns with numeric data by default. This gives us a quick visual overview of the data.

```python
# Creating a line plot
air_quality.plot()
plt.show()
```

### Step 4: Create a Plot for a Specific Column

To plot a specific column, we can use the selection method in combination with the plot method.

```python
# Creating a plot for a specific column
air_quality["station_paris"].plot()
plt.show()
```

### Step 5: Create a Scatter Plot

To visually compare the NO2 values measured in London versus Paris, we can create a scatter plot.

```python
# Creating a scatter plot
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()
```

### Step 6: Create a Box Plot

A box plot gives us a good overview of the data distribution. We can create a box plot for our air quality data.

```python
# Creating a box plot
air_quality.plot.box()
plt.show()
```

### Step 7: Create Subplots for Each Column

We can create separate subplots for each of the data columns using the subplots argument.

```python
# Creating subplots for each column
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()
```

### Step 8: Customize and Save the Plot

We can further customize the plot using Matplotlib's customization options. We can also save the plot to a file.

```python
# Customizing and saving the plot
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ concentration")
fig.savefig("no2_concentrations.png")
plt.show()
```

## Summary

In this lab, we have learned how to create various types of plots using Pandas. We have also learned how to customize and save these plots. This knowledge will be very useful for data analysis and visualization tasks.
