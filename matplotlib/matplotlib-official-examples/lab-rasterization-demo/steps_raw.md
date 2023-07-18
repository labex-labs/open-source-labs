# Rasterization Lab

## Introduction

In this lab, you will learn about rasterization for vector graphics. Rasterization is a process of converting vector graphics into a raster image (pixels). It can speed up rendering and produce smaller files for large data sets, but comes at the cost of a fixed resolution. We will be using Python Matplotlib library to illustrate the concept of rasterization.

## Steps

### Step 1: Import libraries

We need to import the required libraries before we start.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create data

We will create some data which will be used to illustrate the rasterization concept.

```python
d = np.arange(100).reshape(10, 10)  # the values to be color-mapped
x, y = np.meshgrid(np.arange(11), np.arange(11))

theta = 0.25*np.pi
xx = x*np.cos(theta) - y*np.sin(theta)  # rotate x by -theta
yy = x*np.sin(theta) + y*np.cos(theta)  # rotate y by -theta
```

### Step 3: Create a figure with four subplots

We will create a figure with four subplots to illustrate the different aspects of rasterization.

```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout="constrained")
```

### Step 4: Create a pcolormesh plot without rasterization

We will create a pcolormesh plot without rasterization to illustrate the difference between rasterization and non-rasterization.

```python
ax1.set_aspect(1)
ax1.pcolormesh(xx, yy, d)
ax1.set_title("No Rasterization")
```

### Step 5: Create a pcolormesh plot with rasterization

We will create a pcolormesh plot with rasterization to illustrate how rasterization can speed up rendering and produce smaller files.

```python
ax2.set_aspect(1)
ax2.set_title("Rasterization")
ax2.pcolormesh(xx, yy, d, rasterized=True)
```

### Step 6: Create a pcolormesh plot with an overlaid text without rasterization

We will create a pcolormesh plot with an overlaid text without rasterization to illustrate how vector graphics can maintain the advantages of vector graphics for some artists such as the axes and text.

```python
ax3.set_aspect(1)
ax3.pcolormesh(xx, yy, d)
ax3.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax3.transAxes)
ax3.set_title("No Rasterization")
```

### Step 7: Create a pcolormesh plot with an overlaid text with rasterization

We will create a pcolormesh plot with an overlaid text with rasterization to illustrate how rasterization can enable vector graphics to maintain the advantages of vector graphics for some artists such as the axes and text.

```python
ax4.set_aspect(1)
m = ax4.pcolormesh(xx, yy, d, zorder=-10)
ax4.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax4.transAxes)
ax4.set_rasterization_zorder(0)
ax4.set_title("Rasterization z$<-10$")
```

### Step 8: Save the figures

We will save the figures in pdf and eps format.

```python
plt.savefig("test_rasterization.pdf", dpi=150)
plt.savefig("test_rasterization.eps", dpi=150)

if not plt.rcParams["text.usetex"]:
    plt.savefig("test_rasterization.svg", dpi=150)
    # svg backend currently ignores the dpi
```

## Summary

In this lab, we learned about rasterization for vector graphics. We used Python Matplotlib library to illustrate the concept of rasterization. We created a figure with four subplots to illustrate the different aspects of rasterization. We also learned how rasterization can speed up rendering and produce smaller files for large data sets, but comes at the cost of a fixed resolution. We also learned how rasterization can enable vector graphics to maintain the advantages of vector graphics for some artists such as the axes and text.
