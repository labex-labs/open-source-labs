# Species Distribution Modeling

## Introduction

In this lab, we will learn how to model species' geographic distributions using machine learning. This is an important problem in conservation biology, as it helps us understand the distribution of different species and design effective conservation strategies. We will use a dataset of two South American mammals given past observations and 14 environmental variables. We will use the OneClassSVM algorithm from the scikit-learn library to model the geographic distribution of these two species.

## Steps

### Step 1: Import Libraries

In this step, we will import the necessary libraries for our analysis. We will import the scikit-learn library for machine learning, numpy for numerical computing, and matplotlib for visualization.

```python
from time import time

import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import Bunch
from sklearn.datasets import fetch_species_distributions
from sklearn import svm, metrics
```

### Step 2: Load Data

In this step, we will load the data from the scikit-learn library. We will use the fetch_species_distributions function to load the data of two South American mammals given past observations and 14 environmental variables.

```python
# Load the compressed data
data = fetch_species_distributions()
```

### Step 3: Construct Map Grid

In this step, we will construct the map grid from the data object. We will create a function called construct_grids that takes the data object as input and returns the xgrid and ygrid.

```python
def construct_grids(batch):
    """Construct the map grid from the batch object

    Parameters
    ----------
    batch : Batch object
        The object returned by fetch_species_distributions

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

# Construct the map grid
xgrid, ygrid = construct_grids(data)
```

### Step 4: Create Species Bunch

In this step, we will create a bunch with information about a particular organism. We will create a function called create_species_bunch that takes the species name, train, test, coverages, xgrid, and ygrid as input and returns a bunch object.

```python
def create_species_bunch(species_name, train, test, coverages, xgrid, ygrid):
    """Create a bunch with information about a particular organism

    This will use the test/train record arrays to extract the
    data specific to the given species name.
    """
    bunch = Bunch(name=" ".join(species_name.split("_")[:2]))
    species_name = species_name.encode("ascii")
    points = dict(test=test, train=train)

    for label, pts in points.items():
        # choose points associated with the desired species
        pts = pts[pts["species"] == species_name]
        bunch["pts_%s" % label] = pts

        # determine coverage values for each of the training & testing points
        ix = np.searchsorted(xgrid, pts["dd long"])
        iy = np.searchsorted(ygrid, pts["dd lat"])
        bunch["cov_%s" % label] = coverages[:, -iy, ix].T

    return bunch

# Create species bunch
BV_bunch = create_species_bunch(
    "bradypus_variegatus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
MM_bunch = create_species_bunch(
    "microryzomys_minutus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
```

### Step 5: Fit OneClassSVM

In this step, we will fit the OneClassSVM model to the training data. We will standardize the features and fit the OneClassSVM model to the training data.

```python
# Standardize features
mean = BV_bunch.cov_train.mean(axis=0)
std = BV_bunch.cov_train.std(axis=0)
train_cover_std = (BV_bunch.cov_train - mean) / std

# Fit OneClassSVM
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.5)
clf.fit(train_cover_std)
```

### Step 6: Predict Species Distribution

In this step, we will predict the species distribution using the OneClassSVM model. We will predict the species distribution using the training data and plot the results.

```python
# Predict species distribution using the training data
Z = np.ones((data.Ny, data.Nx), dtype=np.float64)

# We'll predict only for the land points.
idx = np.where(data.coverages[6] > -9999)
coverages_land = data.coverages[:, idx[0], idx[1]].T

pred = clf.decision_function((coverages_land - mean) / std)
Z *= pred.min()
Z[idx[0], idx[1]] = pred

levels = np.linspace(Z.min(), Z.max(), 25)
Z[data.coverages[6] == -9999] = -9999

# plot contours of the prediction
plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.Reds)
plt.colorbar(format="%.2f")

# scatter training/testing points
plt.scatter(
    BV_bunch.pts_train["dd long"],
    BV_bunch.pts_train["dd lat"],
    s=2**2,
    c="black",
    marker="^",
    label="train",
)
plt.scatter(
    BV_bunch.pts_test["dd long"],
    BV_bunch.pts_test["dd lat"],
    s=2**2,
    c="black",
    marker="x",
    label="test",
)
plt.legend()
plt.title(BV_bunch.name)
plt.axis("equal")
```

### Step 7: Compute AUC

In this step, we will compute the area under the ROC curve (AUC) with regards to background points. We will predict the species distribution using the test data and the background points, and compute the AUC.

```python
# Compute AUC with regards to background points
background_points = np.c_[
    np.random.randint(low=0, high=data.Ny, size=10000),
    np.random.randint(low=0, high=data.Nx, size=10000),
].T

pred_background = Z[background_points[0], background_points[1]]
pred_test = clf.decision_function((BV_bunch.cov_test - mean) / std)
scores = np.r_[pred_test, pred_background]
y = np.r_[np.ones(pred_test.shape), np.zeros(pred_background.shape)]
fpr, tpr, thresholds = metrics.roc_curve(y, scores)
roc_auc = metrics.auc(fpr, tpr)
plt.text(-35, -70, "AUC: %.3f" % roc_auc, ha="right")
print("\n Area under the ROC curve : %f" % roc_auc)
```

### Step 8: Plot Species Distribution

In this step, we will plot the species distribution for both species using the functions and models we have created.

```python
# Plot species distribution
plot_species_distribution()
plt.show()
```

## Summary

In this lab, we learned how to model species' geographic distributions using machine learning. We used the OneClassSVM algorithm from the scikit-learn library to model the geographic distribution of two South American mammals given past observations and 14 environmental variables. We also learned how to plot the species distribution and compute the area under the ROC curve to evaluate the performance of our model.
