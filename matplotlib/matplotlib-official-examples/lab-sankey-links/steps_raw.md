# Python Matplotlib Tutorial - Creating a Long Chain of Connections using Sankey

## Introduction

In this lab, we will learn how to use the `Sankey` class from the `matplotlib.sankey` module to create a long chain of connections using Python Matplotlib.

## Steps

### Step 1: Import necessary libraries and modules

We begin by importing the necessary libraries and modules. We will be using `matplotlib.pyplot` and `matplotlib.sankey`.

```python
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey
```

### Step 2: Define the number of links per side

Next, we define the number of links per side in our chain. In this example, we will set it to 6.

```python
links_per_side = 6
```

### Step 3: Define the `side` function

Now, we define the `side` function which generates a side chain.

```python
def side(sankey, n=1):
    """Generate a side chain."""
    prior = len(sankey.diagrams)
    for i in range(0, 2*n, 2):
        sankey.add(flows=[1, -1], orientations=[-1, -1],
                   patchlabel=str(prior + i),
                   prior=prior + i - 1, connect=(1, 0), alpha=0.5)
        sankey.add(flows=[1, -1], orientations=[1, 1],
                   patchlabel=str(prior + i + 1),
                   prior=prior + i, connect=(1, 0), alpha=0.5)
```

### Step 4: Define the `corner` function

Next, we define the `corner` function which generates a corner link.

```python
def corner(sankey):
    """Generate a corner link."""
    prior = len(sankey.diagrams)
    sankey.add(flows=[1, -1], orientations=[0, 1],
               patchlabel=str(prior), facecolor='k',
               prior=prior - 1, connect=(1, 0), alpha=0.5)
```

### Step 5: Create the figure and axis objects

Now, we create the `figure` and `axis` objects using `plt.subplots()`.

```python
fig, ax = plt.subplots()
```

### Step 6: Create the `Sankey` object

Next, we create the `Sankey` object using the `ax` object and set the `unit` to `None`.

```python
sankey = Sankey(ax=ax, unit=None)
```

### Step 7: Add the first diagram

We add the first diagram using `sankey.add()` with `flows=[1, -1]` and `orientations=[0, 1]`.

```python
sankey.add(flows=[1, -1], orientations=[0, 1],
           patchlabel="0", facecolor='k',
           rotation=45)
```

### Step 8: Add side chains and corner links

Now, we add the side chains and corner links using the `side()` and `corner()` functions.

```python
side(sankey, n=links_per_side)
corner(sankey)
side(sankey, n=links_per_side)
corner(sankey)
side(sankey, n=links_per_side)
corner(sankey)
side(sankey, n=links_per_side)
```

### Step 9: Finish and display the Sankey diagram

Finally, we finish the `Sankey` diagram using `sankey.finish()` and display it using `plt.show()`.

```python
sankey.finish()
plt.show()
```

## Summary

In this lab, we learned how to use the `Sankey` class from the `matplotlib.sankey` module to create a long chain of connections using Python Matplotlib. We defined the `side` and `corner` functions to generate the side chains and corner links respectively. We also added the first diagram, side chains, and corner links using the `Sankey` object and displayed the diagram using `plt.show()`.
