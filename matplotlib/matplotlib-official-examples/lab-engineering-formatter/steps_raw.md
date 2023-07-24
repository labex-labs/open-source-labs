# Labeling Ticks Using Engineering Notation

## Introduction

In data visualization, it is essential to label the ticks on axes accurately. The `EngFormatter` in Matplotlib is a class that enables one to label the ticks on an axis using engineering notation. Engineering notation is a mathematical representation of numbers that uses powers of ten with a multiple of three. It is a concise way to express large or small numbers that are difficult to read or write in standard notation. In this lab, we will learn how to label ticks on an axis using engineering notation.

## Steps

### Step 1: Import Required Libraries

The first step is to import the required libraries. In this lab, we will use `Matplotlib`, `NumPy`, and `EngFormatter`.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import EngFormatter
```

### Step 2: Create Artificial Data

We need to create some artificial data to plot. In this lab, we will plot the log of the frequency (in Hz) against the log of the power (in Watts). We will use the `numpy` library to generate the data.

```python
# Fixing random state for reproducibility
prng = np.random.RandomState(19680801)

# Create artificial data to plot.
# The x data span over several decades to demonstrate several SI prefixes.
xs = np.logspace(1, 9, 100)
ys = (0.8 + 0.4 * prng.uniform(size=100)) * np.log10(xs)**2
```

### Step 3: Create the Figure and Subplots

We need to create a figure and subplots to display the data. In this lab, we will create two subplots, side by side.

```python
# Figure width is doubled (2*6.4) to display nicely 2 subplots side by side.
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(7, 9.6))
for ax in (ax0, ax1):
    ax.set_xscale('log')
```

### Step 4: Label the Ticks Using Engineering Notation

We will now label the ticks on the x-axis using engineering notation. In the first subplot, we will use the default settings, and in the second subplot, we will use the options `places` and `sep` to specify the number of digits after the decimal point and the separator between the number and the prefix/unit.

```python
# Demo of the default settings, with a user-defined unit label.
ax0.set_title('Full unit ticklabels, w/ default precision & space separator')
formatter0 = EngFormatter(unit='Hz')
ax0.xaxis.set_major_formatter(formatter0)
ax0.plot(xs, ys)
ax0.set_xlabel('Frequency')

# Demo of the options `places` (number of digit after decimal point) and
# `sep` (separator between the number and the prefix/unit).
ax1.set_title('SI-prefix only ticklabels, 1-digit precision & '
              'thin space separator')
formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
ax1.xaxis.set_major_formatter(formatter1)
ax1.plot(xs, ys)
ax1.set_xlabel('Frequency [Hz]')
```

### Step 5: Display the Plot

We will now display the plot using the `plt.show()` function.

```python
plt.tight_layout()
plt.show()
```

## Summary

In this lab, we learned how to label ticks on an axis using engineering notation. We used the `EngFormatter` class in Matplotlib to label the ticks on the x-axis of a plot. We also learned how to create subplots and customize the tick labels using the `EngFormatter` options `places` and `sep`. Engineering notation is a concise and clear way to express large or small numbers that are difficult to read or write in standard notation.
