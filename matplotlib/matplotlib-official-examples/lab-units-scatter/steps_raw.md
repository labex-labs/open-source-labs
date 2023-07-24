# Unit Handling Lab

## Introduction

This lab will guide you through a step-by-step tutorial on how to perform unit conversions over masked arrays using Python Matplotlib.

## Steps

### Step 1: Import Libraries

In this step, we will import the necessary libraries to perform the unit conversions and plotting.

```python
import matplotlib.pyplot as plt
import numpy as np
from basic_units import hertz, minutes, secs
```

### Step 2: Create Masked Array

In this step, we will create a masked array and apply the mask to the data.

```python
# create masked array
data = (1, 2, 3, 4, 5, 6, 7, 8)
mask = (1, 0, 1, 0, 0, 0, 1, 0)
xsecs = secs * np.ma.MaskedArray(data, mask, float)
```

### Step 3: Create Plots

In this step, we will create three plots using the masked array with different units.

```python
# create subplots
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, sharex=True)

# plot 1
ax1.scatter(xsecs, xsecs)
ax1.yaxis.set_units(secs)

# plot 2
ax2.scatter(xsecs, xsecs, yunits=hertz)

# plot 3
ax3.scatter(xsecs, xsecs, yunits=minutes)

# set labels
ax1.set_ylabel('Seconds')
ax2.set_ylabel('Hertz')
ax3.set_ylabel('Minutes')
ax3.set_xlabel('Time')
```

### Step 4: Display Plots

In this step, we will display the plots that were created in the previous step.

```python
# display plot
plt.show()
```

## Summary

In this lab, we have learned how to perform unit conversions over masked arrays using Python Matplotlib. We have created a masked array and applied a mask to the data. We have also created three plots using the masked array with different units and displayed them.
