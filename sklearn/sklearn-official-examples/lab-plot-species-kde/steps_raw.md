# Kernel Density Estimate of Species Distributions

## Introduction

This lab demonstrates an example of a neighbors-based query (in particular a kernel density estimate) on geospatial data, using a Ball Tree built upon the Haversine distance metric -- i.e. distances over points in latitude/longitude. The dataset is provided by Phillips et. al. (2006). The example uses the basemap library to plot the coastlines and national boundaries of South America.

## Steps

### Step 1: Import Required Libraries

The first step is to import the required libraries for this lab. We will be using numpy, matplotlib, fetch_species_distributions, and KernelDensity libraries in this lab.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_species_distributions
from sklearn.neighbors import KernelDensity
```

### Step 2: Load Data

The next step is to load the data provided by Phillips et. al. (2006). The dataset contains two species that we will use to demonstrate the kernel density estimate.

```python
data = fetch_species_distributions()
species_names = ["Bradypus Variegatus", "Microryzomys Minutus"]
```

### Step 3: Prepare Data

We will now prepare the data for kernel density estimation. We will extract the latitude and longitude information from the dataset and convert them to radians.

```python
Xtrain = np.vstack([data["train"]["dd lat"], data["train"]["dd long"]]).T
ytrain = np.array(
    [d.decode("ascii").startswith("micro") for d in data["train"]["species"]],
    dtype="int",
)
Xtrain *= np.pi / 180.0  # Convert lat/long to radians
```

### Step 4: Construct Grids

We will now construct the map grid from the batch object. We will use the `construct_grids` function to achieve this.

```python
def construct_grids(batch):
    """Construct the map grid from the batch object

    Parameters
    ----------
    batch : Batch object
        The object returned by :func:`fetch_species_distributions`

    Returns
    -------
    (xgrid, ygrid) : 1-D arrays
        The grid corresponding to the values in batch.coverages
    """
    # x,y coordinates for corner cells
    xmin = batch.x_left_lower_corner + batch.grid_size
    xmax = xmin + (batch.Nx * batch.grid_size)
    ymin = batch.y_left_lower_corner + batch.grid_size
    ymax = ymin + (batch.Ny * batch.grid_size)

    # x coordinates of the grid cells
    xgrid = np.arange(xmin, xmax, batch.grid_size)
    # y coordinates of the grid cells
    ygrid = np.arange(ymin, ymax, batch.grid_size)

    return (xgrid, ygrid)

# Call the function and store the results in xgrid and ygrid
xgrid, ygrid = construct_grids(data)
```

### Step 5: Prepare the Data Grid

We will set up the data grid for the contour plot. We will use the `construct_grids` function to achieve this.

```python
X, Y = np.meshgrid(xgrid[::5], ygrid[::5][::-1])
land_reference = data.coverages[6][::5, ::5]
land_mask = (land_reference > -9999).ravel()

xy = np.vstack([Y.ravel(), X.ravel()]).T
xy = xy[land_mask]
xy *= np.pi / 180.0
```

### Step 6: Plot Map of South America

We will now plot the map of South America with the distributions of each species.

```python
fig = plt.figure()
fig.subplots_adjust(left=0.05, right=0.95, wspace=0.05)

for i in range(2):
    plt.subplot(1, 2, i + 1)

    print(" - computing KDE in spherical coordinates")
    kde = KernelDensity(
        bandwidth=0.04, metric="haversine", kernel="gaussian", algorithm="ball_tree"
    )
    kde.fit(Xtrain[ytrain == i])

    Z = np.full(land_mask.shape[0], -9999, dtype="int")
    Z[land_mask] = np.exp(kde.score_samples(xy))
    Z = Z.reshape(X.shape)

    levels = np.linspace(0, Z.max(), 25)
    plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.Reds)

    if basemap:
        print(" - plot coastlines using basemap")
        m = Basemap(
            projection="cyl",
            llcrnrlat=Y.min(),
            urcrnrlat=Y.max(),
            llcrnrlon=X.min(),
            urcrnrlon=X.max(),
            resolution="c",
        )
        m.drawcoastlines()
        m.drawcountries()
    else:
        print(" - plot coastlines from coverage")
        plt.contour(
            X, Y, land_reference, levels=[-9998], colors="k", linestyles="solid"
        )
        plt.xticks([])
        plt.yticks([])

    plt.title(species_names[i])

plt.show()
```

## Summary

In this lab, we learned how to perform kernel density estimation on geospatial data. We used the Phillips et. al. (2006) dataset to demonstrate this technique. We also learned how to plot the map of South America with the distributions of each species using the basemap library.
