# Python Matplotlib Tutorial

## Introduction

In this lab, we will learn how to create shaded relief plots using Python Matplotlib. Shaded relief plots are useful for visualizing terrain data, as they use shading to represent variations in elevation.

## Steps

### Step 1: Import Libraries

We will start by importing the necessary libraries.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cbook
from matplotlib.colors import LightSource
```

### Step 2: Load Data

Next, we will load the sample data that we will use for this tutorial. We will use the `jacksboro_fault_dem.npz` file, which contains elevation data.

```python
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
elev = dem['elevation']
```

### Step 3: Create Shaded Relief Plots

We will now create the shaded relief plots using the `LightSource` class. We will create two subplots, one with a colormapped data and the other with illumination intensity.

```python
# Illuminate the scene from the northwest
ls = LightSource(azdeg=315, altdeg=45)

fig, axs = plt.subplots(ncols=2, nrows=2)
for ax in axs.flat:
    ax.set(xticks=[], yticks=[])

axs[0, 0].imshow(z, cmap=cmap)
axs[0, 0].set(xlabel='Colormapped Data')

axs[0, 1].imshow(ls.hillshade(z, vert_exag=ve), cmap='gray')
axs[0, 1].set(xlabel='Illumination Intensity')
```

We will create two more subplots, one with the `blend_mode` set to "hsv" and the other set to "overlay".

```python
rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='hsv')
axs[1, 0].imshow(rgb)
axs[1, 0].set(xlabel='Blend Mode: "hsv" (default)')

rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='overlay')
axs[1, 1].imshow(rgb)
axs[1, 1].set(xlabel='Blend Mode: "overlay"')
```

### Step 4: Display the Plots

Finally, we will display the plots using `plt.show()`.

```python
plt.show()
```

## Summary

In this lab, we learned how to create shaded relief plots using Python Matplotlib. We loaded sample data and used the `LightSource` class to create four subplots with different shading techniques. We then displayed the plots using `plt.show()`.
