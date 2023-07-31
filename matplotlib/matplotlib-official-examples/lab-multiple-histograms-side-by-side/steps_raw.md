# Producing Multiple Histograms with Matplotlib

## Introduction

Histograms are a great way to visualize the distribution of a dataset, and Matplotlib is one of the most popular Python libraries for creating data visualizations. In this lab, we will use Matplotlib to create side-by-side histograms for multiple datasets.

## Steps

### Step 1: Import necessary libraries

First, we need to import the necessary libraries for our code. We will use Matplotlib and NumPy for our histograms:

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create example datasets

Next, we will create example datasets to use for our histograms. We will create three datasets with 387 data points each:

```python
np.random.seed(19680801)
number_of_data_points = 387
labels = ["A", "B", "C"]
data_sets = [np.random.normal(0, 1, number_of_data_points),
             np.random.normal(6, 1, number_of_data_points),
             np.random.normal(-3, 1, number_of_data_points)]
```

### Step 3: Compute quantities for plotting

Before we can create our histograms, we need to compute some quantities for plotting. We will compute the range of our datasets, the binned data sets, the maximum bin values, and the x-locations for each histogram:

```python
hist_range = (np.min(data_sets), np.max(data_sets))
number_of_bins = 20
binned_data_sets = [
    np.histogram(d, range=hist_range, bins=number_of_bins)[0]
    for d in data_sets
]
binned_maximums = np.max(binned_data_sets, axis=1)
x_locations = np.arange(0, sum(binned_maximums), np.max(binned_maximums))
```

### Step 4: Plot the histograms

Now that we have computed the necessary quantities for plotting, we can create our histograms. We will use the `barh` method to plot horizontal bars for each histogram:

```python
# The bin_edges are the same for all of the histograms
bin_edges = np.linspace(hist_range[0], hist_range[1], number_of_bins + 1)
heights = np.diff(bin_edges)
centers = bin_edges[:-1] + heights / 2

# Cycle through and plot each histogram
fig, ax = plt.subplots()
for x_loc, binned_data in zip(x_locations, binned_data_sets):
    lefts = x_loc - 0.5 * binned_data
    ax.barh(centers, binned_data, height=heights, left=lefts)

ax.set_xticks(x_locations, labels)
ax.set_ylabel("Data values")
ax.set_xlabel("Data sets")
```

### Step 5: Display the histograms

Finally, we can display our histograms using the `show` method:

```python
plt.show()
```

## Summary

In this lab, we learned how to create side-by-side histograms for multiple datasets using Matplotlib. We computed the necessary quantities for plotting, and used the `barh` method to create horizontal bars for each histogram. With these skills, we can create informative visualizations of our data to gain insights and communicate our findings to others.
