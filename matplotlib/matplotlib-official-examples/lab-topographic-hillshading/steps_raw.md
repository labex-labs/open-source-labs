# Topographic Hillshading Lab

## Introduction

This lab demonstrates how to use Matplotlib to create topographic hillshading plots using varying blend modes and vertical exaggeration. The purpose of hillshading is for visual purposes to create a 3D-like effect on 2D maps. In this lab, we will learn how to change the blend modes and vertical exaggeration to achieve different visual effects.

## Steps

### Step 1: Import Required Libraries

We begin by importing the required libraries, including Matplotlib, NumPy, and LightSource.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cbook import get_sample_data
from matplotlib.colors import LightSource
```

### Step 2: Load the Data

Next, we load the sample elevation data using the `get_sample_data` function from Matplotlib. We then extract the elevation data and the cell size of the grid.

```python
dem = get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']
dx, dy = dem['dx'], dem['dy']
```

### Step 3: Specify the Cell Size

If you need topographically accurate vertical exaggeration, or you don't want to guess at what `vert_exag` should be, you'll need to specify the cell size of the grid (i.e. the `dx` and `dy` parameters). Otherwise, any `vert_exag` value you specify will be relative to the grid spacing of your input data. In this step, we calculate the `dx` and `dy` values in meters.

```python
dy = 111200 * dy
dx = 111200 * dx * np.cos(np.radians(dem['ymin']))
```

### Step 4: Specify Light Source and Colormap

We specify the LightSource object by setting the azimuth and altitude of the light source. We also set the colormap to be used in the plot.

```python
ls = LightSource(azdeg=315, altdeg=45)
cmap = plt.cm.gist_earth
```

### Step 5: Create the Plot

We create a 4x3 plot grid to show the hillshaded plots with different blend modes and vertical exaggeration. We first show the hillshade intensity image in the first row, and then place hillshaded plots with different blend modes in the rest of the rows. We use a for loop to iterate through the different vertical exaggeration values and blend modes.

```python
fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(8, 9))
plt.setp(axs.flat, xticks=[], yticks=[])

for col, ve in zip(axs.T, [0.1, 1, 10]):
    col[0].imshow(ls.hillshade(z, vert_exag=ve, dx=dx, dy=dy), cmap='gray')
    for ax, mode in zip(col[1:], ['hsv', 'overlay', 'soft']):
        rgb = ls.shade(z, cmap=cmap, blend_mode=mode,
                       vert_exag=ve, dx=dx, dy=dy)
        ax.imshow(rgb)
```

### Step 6: Label the Plot

We label the rows and columns of the plot grid using the `set_title` and `set_ylabel` functions. We also add a title for the vertical exaggeration and blend mode groups.

```python
for ax, ve in zip(axs[0], [0.1, 1, 10]):
    ax.set_title(f'{ve}', size=18)
for ax, mode in zip(axs[:, 0], ['Hillshade', 'hsv', 'overlay', 'soft']):
    ax.set_ylabel(mode, size=18)

axs[0, 1].annotate('Vertical Exaggeration', (0.5, 1), xytext=(0, 30),
                   textcoords='offset points', xycoords='axes fraction',
                   ha='center', va='bottom', size=20)
axs[2, 0].annotate('Blend Mode', (0, 0.5), xytext=(-30, 0),
                   textcoords='offset points', xycoords='axes fraction',
                   ha='right', va='center', size=20, rotation=90)
fig.subplots_adjust(bottom=0.05, right=0.95)
```

### Step 7: Display the Plot

Finally, we display the plot using the `show` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create topographic hillshading plots using Matplotlib. We used varying blend modes and vertical exaggeration to achieve different visual effects. We also learned how to specify the cell size of the grid for topographically accurate vertical exaggeration.
