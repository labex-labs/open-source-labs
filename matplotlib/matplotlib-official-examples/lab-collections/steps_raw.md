# Matplotlib Collection Tutorial

## Introduction

This tutorial will guide you through creating a visualization using Matplotlib collection. The tutorial will show you how to use LineCollection, PolyCollection, and RegularPolyCollection. The tutorial will also show you how to use the offsets and offset_transform keyword arguments of the LineCollection and PolyCollection to set the positions of the spirals. The tutorial will also show you how to use the RegularPolyCollection to make regular polygons.

## Steps

### Step 1: Import necessary libraries

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import collections, transforms
```

The first step is to import the necessary libraries. We will be using Matplotlib and Numpy for this tutorial.

### Step 2: Create spirals

```python
nverts = 50
npts = 100

# Make some spirals
r = np.arange(nverts)
theta = np.linspace(0, 2*np.pi, nverts)
xx = r * np.sin(theta)
yy = r * np.cos(theta)
spiral = np.column_stack([xx, yy])
```

The next step is to create spirals using Numpy. We will be using the sin and cos functions to create the spirals.

### Step 3: Create offsets

```python
# Fixing random state for reproducibility
rs = np.random.RandomState(19680801)

# Make some offsets
xyo = rs.randn(npts, 2)
```

The third step is to create offsets using Numpy. We will be using the random function to create the offsets.

### Step 4: Create LineCollection using offsets

```python
col = collections.LineCollection(
    [spiral], offsets=xyo, offset_transform=ax1.transData)
trans = fig.dpi_scale_trans + transforms.Affine2D().scale(1.0/72.0)
col.set_transform(trans)
col.set_color(colors)

ax1.add_collection(col, autolim=True)
ax1.autoscale_view()

ax1.set_title('LineCollection using offsets')
```

The fourth step is to create a LineCollection using offsets. We will be using the LineCollection to create curves with offsets. We will also be using the offset_transform to set the positions of the curves.

### Step 5: Create PolyCollection using offsets

```python
col = collections.PolyCollection(
    [spiral], offsets=xyo, offset_transform=ax2.transData)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans)
col.set_color(colors)

ax2.add_collection(col, autolim=True)
ax2.autoscale_view()

ax2.set_title('PolyCollection using offsets')
```

The fifth step is to create a PolyCollection using offsets. We will be using the PolyCollection to fill the curves with colors. We will also be using the offset_transform to set the positions of the curves.

### Step 6: Create RegularPolyCollection using offsets

```python
col = collections.RegularPolyCollection(
    7, sizes=np.abs(xx) * 10.0, offsets=xyo, offset_transform=ax3.transData)
trans = transforms.Affine2D().scale(fig.dpi / 72.0)
col.set_transform(trans)
col.set_color(colors)

ax3.add_collection(col, autolim=True)
ax3.autoscale_view()

ax3.set_title('RegularPolyCollection using offsets')
```

The sixth step is to create a RegularPolyCollection using offsets. We will be using the RegularPolyCollection to create regular polygons with offsets. We will also be using the offset_transform to set the positions of the polygons.

### Step 7: Create successive data offsets

```python
# Simulate a series of ocean current profiles, successively
# offset by 0.1 m/s so that they form what is sometimes called
# a "waterfall" plot or a "stagger" plot.

nverts = 60
ncurves = 20
offs = (0.1, 0.0)

yy = np.linspace(0, 2*np.pi, nverts)
ym = np.max(yy)
xx = (0.2 + (ym - yy) / ym) ** 2 * np.cos(yy - 0.4) * 0.5
segs = []
for i in range(ncurves):
    xxx = xx + 0.02*rs.randn(nverts)
    curve = np.column_stack([xxx, yy * 100])
    segs.append(curve)

col = collections.LineCollection(segs, offsets=offs)
ax4.add_collection(col, autolim=True)
col.set_color(colors)
ax4.autoscale_view()

ax4.set_title('Successive data offsets')
ax4.set_xlabel('Zonal velocity component (m/s)')
ax4.set_ylabel('Depth (m)')
ax4.set_ylim(ax4.get_ylim()[::-1])
```

The seventh step is to create successive data offsets. We will be using the LineCollection to create curves with successive offsets.

## Summary

This tutorial has shown you how to use Matplotlib collection to create visualizations. You have learned how to use LineCollection, PolyCollection, and RegularPolyCollection to create curves and polygons. You have also learned how to use the offsets and offset_transform keyword arguments of the LineCollection and PolyCollection to set the positions of the spirals.
