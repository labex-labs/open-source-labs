# Custom Hillshading in a 3D Surface Plot

## Introduction

This lab demonstrates how to use custom hillshading in a 3D surface plot using Python Matplotlib. Hillshading is the use of light and shadow to enhance the perception of depth and relief in a 3D plot. By customizing the hillshading, we can create a more visually appealing and informative plot.

## Steps

### Step 1: Load and format data

In this step, we will load and format the data for the 3D surface plot. We will be using a sample dataset called "jacksboro_fault_dem.npz".

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cbook, cm
from matplotlib.colors import LightSource

# Load and format data
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']
nrows, ncols = z.shape
x = np.linspace(dem['xmin'], dem['xmax'], ncols)
y = np.linspace(dem['ymin'], dem['ymax'], nrows)
x, y = np.meshgrid(x, y)

region = np.s_[5:50, 5:50]
x, y, z = x[region], y[region], z[region]
```

### Step 2: Set up plot

In this step, we will set up the plot for the 3D surface plot. We will be using a LightSource object to customize the hillshading.

```python
# Set up plot
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

ls = LightSource(270, 45)
# To use a custom hillshading mode, override the built-in shading and pass
# in the rgb colors of the shaded surface calculated from "shade".
rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)

plt.show()
```

### Step 3: Customize Hillshading

In this step, we will customize the hillshading by overriding the built-in shading and passing in the RGB colors of the shaded surface calculated from "shade".

```python
# Set up plot
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

ls = LightSource(270, 45)
# To use a custom hillshading mode, override the built-in shading and pass
# in the rgb colors of the shaded surface calculated from "shade".
rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)

plt.show()
```

### Step 4: Review and revise

Review the code and make any necessary revisions. Ensure that the code is accurate and well-commented.

## Summary

In this lab, we learned how to use custom hillshading in a 3D surface plot using Python Matplotlib. By customizing the hillshading, we were able to create a more visually appealing and informative plot.
