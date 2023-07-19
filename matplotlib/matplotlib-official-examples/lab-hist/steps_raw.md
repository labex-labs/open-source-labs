# Matplotlib Histogram Plotting Lab

## Introduction

In this lab, we will learn how to plot histograms with Matplotlib. We will generate data and plot a simple histogram, update histogram colors, plot a 2D histogram, and customize your histogram.

## Steps

### Step 1: Generate Data and Plot a Simple Histogram

To generate a 1D histogram, we only need a single vector of numbers. For a 2D histogram, we'll need a second vector. We'll generate both below, and show the histogram for each vector.

```python
import matplotlib.pyplot as plt
import numpy as np

# Create a random number generator with a fixed seed for reproducibility
rng = np.random.default_rng(19680801)

N_points = 100000
n_bins = 20

# Generate two normal distributions
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the *bins* keyword argument.
axs[0].hist(dist1, bins=n_bins)
axs[1].hist(dist2, bins=n_bins)

plt.show()
```

### Step 2: Updating Histogram Colors

The histogram method returns (among other things) a `patches` object. This gives us access to the properties of the objects drawn. Using this, we can edit the histogram to our liking. Let's change the color of each bar based on its y value.

```python
# N is the count in each bin, bins is the lower-limit of the bin
N, bins, patches = axs[0].hist(dist1, bins=n_bins)

# We'll color code by height, but you could use any scalar
fracs = N / N.max()

# we need to normalize the data to 0..1 for the full range of the colormap
norm = colors.Normalize(fracs.min(), fracs.max())

# Now, we'll loop through our objects and set the color of each accordingly
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

# We can also normalize our inputs by the total number of counts
axs[1].hist(dist1, bins=n_bins, density=True)

# Now we format the y-axis to display percentage
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))

plt.show()
```

### Step 3: Plot a 2D Histogram

To plot a 2D histogram, one only needs two vectors of the same length, corresponding to each axis of the histogram.

```python
fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(dist1, dist2)

plt.show()
```

### Step 4: Customizing your Histogram

Customizing a 2D histogram is similar to the 1D case, you can control visual components such as the bin size or color normalization.

```python
fig, axs = plt.subplots(3, 1, figsize=(5, 15), sharex=True, sharey=True,
                        tight_layout=True)

# We can increase the number of bins on each axis
axs[0].hist2d(dist1, dist2, bins=40)

# As well as define normalization of the colors
axs[1].hist2d(dist1, dist2, bins=40, norm=colors.LogNorm())

# We can also define custom numbers of bins for each axis
axs[2].hist2d(dist1, dist2, bins=(80, 10), norm=colors.LogNorm())

plt.show()
```

## Summary

In this lab, we learned how to plot histograms with Matplotlib. We generated data and plotted a simple histogram, updated histogram colors, plotted a 2D histogram, and customized our histogram. We can use these techniques to visualize and analyze data in a variety of contexts.
