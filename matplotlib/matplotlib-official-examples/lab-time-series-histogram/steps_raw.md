# Python Matplotlib Time Series Histogram Lab

## Introduction

This lab demonstrates how to efficiently visualize large numbers of time series in a way that could potentially reveal hidden substructure and patterns that are not immediately obvious and display them in a visually appealing way.

## Steps

### Step 1: Import Required Libraries

In this step, we will import the required libraries for this lab.

```python
import time
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate Data

In this step, we will generate multiple sinusoidal "signal" series that are buried under a larger number of random walk "noise/background" series. We will generate unbiased Gaussian random walks and sinusoidal signals.

```python
# Fix random state for reproducibility
np.random.seed(19680801)

# Make some data; a 1D random walk + small fraction of sine waves
num_series = 1000
num_points = 100
SNR = 0.10  # Signal to Noise Ratio
x = np.linspace(0, 4 * np.pi, num_points)

# Generate unbiased Gaussian random walks
Y = np.cumsum(np.random.randn(num_series, num_points), axis=-1)

# Generate sinusoidal signals
num_signal = round(SNR * num_series)
phi = (np.pi / 8) * np.random.randn(num_signal, 1)  # small random offset
Y[-num_signal:] = (
    np.sqrt(np.arange(num_points))  # random walk RMS scaling factor
    * (np.sin(x - phi)
       + 0.05 * np.random.randn(num_signal, num_points))  # small random noise
)
```

### Step 3: Visualize Data with Line Plot

In this step, we will visualize the generated data with a line plot.

```python
# Plot series using `plot` and a small value of `alpha`.
# With this view, it is very difficult to observe the sinusoidal behavior because of how many overlapping series there are.
# It also takes a bit of time to run because so many individual artists need to be generated.
tic = time.time()
plt.plot(x, Y.T, color="C0", alpha=0.1)
toc = time.time()
plt.title("Line plot with alpha")
plt.show()
print(f"{toc-tic:.3f} sec. elapsed")
```

### Step 4: Visualize Data with 2D Histogram - Log Color Scale

In this step, we will convert the multiple time series into a histogram. Not only will the hidden signal be more visible, but it is also a much quicker procedure. We will plot (x, y) points in 2D histogram with a log color scale.

```python
tic = time.time()

# Linearly interpolate between the points in each time series
num_fine = 800
x_fine = np.linspace(x.min(), x.max(), num_fine)
y_fine = np.concatenate([np.interp(x_fine, x, y_row) for y_row in Y])
x_fine = np.broadcast_to(x_fine, (num_series, num_fine)).ravel()

# Plot (x, y) points in 2d histogram with log colorscale
# It is pretty evident that there is some kind of structure under the noise
# You can tune vmax to make signal more visible
cmap = plt.colormaps["plasma"]
cmap = cmap.with_extremes(bad=cmap(0))
h, xedges, yedges = np.histogram2d(x_fine, y_fine, bins=[400, 100])
pcm = plt.pcolormesh(xedges, yedges, h.T, cmap=cmap,
                         norm="log", vmax=1.5e2, rasterized=True)
plt.colorbar(pcm, label="# points", pad=0)
plt.title("2D Histogram and Log Color Scale")
plt.show()

toc = time.time()
print(f"{toc-tic:.3f} sec. elapsed")
```

### Step 5: Visualize Data with 2D Histogram - Linear Color Scale

In this step, we will visualize data with a linear color scale.

```python
# Same data but on linear color scale
pcm = plt.pcolormesh(xedges, yedges, h.T, cmap=cmap,
                         vmax=1.5e2, rasterized=True)
plt.colorbar(pcm, label="# points", pad=0)
plt.title("2D Histogram and Linear Color Scale")
plt.show()
```

## Summary

In this lab, we learned how to efficiently visualize large numbers of time series in a way that could potentially reveal hidden substructure and patterns that are not immediately obvious and display them in a visually appealing way. We generated multiple sinusoidal "signal" series that are buried under a larger number of random walk "noise/background" series, and we visualized the data with a line plot and 2D histogram with log and linear color scales.
