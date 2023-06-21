# Python Matplotlib Tutorial

## Introduction

In this tutorial, you will learn how to create a plot with two y-axes using Matplotlib. The plot will display two sets of data with different units of measurement on different scales. This type of plot is commonly used in scientific research to visualize relationships between variables that are not directly comparable.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries. We will be using Matplotlib and its parasite_axes module to create the plot.

```python
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from mpl_toolkits.axes_grid1.parasite_axes import HostAxes
```

### Step 2: Define Data

Next, we need to define the data that will be plotted. In this example, we have a set of observations with four variables: name, angular proper motion, angular proper motion error, and distance. We will convert the angular proper motion to linear velocity and plot it against the FWHM (full width at half maximum) of the observations.

```python
obs = [["01_S1", 3.88, 0.14, 1970, 63],
       ["01_S4", 5.6, 0.82, 1622, 150],
       ["02_S1", 2.4, 0.54, 1570, 40],
       ["03_S1", 4.1, 0.62, 2380, 170]]

# Conversion factor from angular proper motion to linear velocity
pm_to_kms = 1./206265.*2300*3.085e18/3.15e7/1.e5
```

### Step 3: Create the Plot

We will now create the plot using the HostAxes and twin() functions from the parasite_axes module. HostAxes is used to create the main plot, and twin() is used to create the secondary y-axis.

```python
fig = plt.figure()

# Create HostAxes object
ax_kms = fig.add_subplot(axes_class=HostAxes, aspect=1)

# Create secondary y-axis with transformed coordinates
aux_trans = mtransforms.Affine2D().scale(pm_to_kms, 1.)
ax_pm = ax_kms.twin(aux_trans)

# Plot the data
for n, ds, dse, w, we in obs:
    time = ((2007 + (10. + 4/30.)/12) - 1988.5)
    v = ds / time * pm_to_kms
    ve = dse / time * pm_to_kms
    ax_kms.errorbar([v], [w], xerr=[ve], yerr=[we], color="k")

# Set the axis labels
ax_kms.axis["bottom"].set_label("Linear velocity at 2.3 kpc [km/s]")
ax_kms.axis["left"].set_label("FWHM [km/s]")
ax_pm.axis["top"].set_label(r"Proper Motion [$''$/yr]")

# Hide the tick labels on the secondary y-axis
ax_pm.axis["right"].major_ticklabels.set_visible(False)

# Set the plot limits
ax_kms.set_xlim(950, 3700)
ax_kms.set_ylim(950, 3100)
```

### Step 4: Display the Plot

Finally, we will display the plot using the plt.show() function.

```python
plt.show()
```

## Summary

In this tutorial, you learned how to create a plot with two y-axes using Matplotlib. You learned how to define the data, create the plot, and display the plot. This type of plot is useful for visualizing relationships between variables that are not directly comparable.
