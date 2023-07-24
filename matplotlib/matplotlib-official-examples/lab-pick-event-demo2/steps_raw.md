# Step-by-Step Lab: Computing the Mean and Standard Deviation of 100 Data Sets

## Introduction

In this lab, we will use Python's Matplotlib library to compute the mean (mu) and standard deviation (sigma) of 100 data sets and plot mu vs. sigma. We will also add interactivity to the plot so that when you click on one of the (mu, sigma) points, the raw data from the dataset that generated this point will be plotted.

## Steps

### Step 1: Generate Random Data

First, we need to generate 100 random datasets, each containing 1000 random numbers between 0 and 1. We will use numpy's random module to generate the random data.

```python
import numpy as np

np.random.seed(19680801)

X = np.random.rand(100, 1000)
```

### Step 2: Compute Mean and Standard Deviation

Next, we will compute the mean and standard deviation of each of the 100 datasets. We will use numpy's mean and std functions to compute these values.

```python
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)
```

### Step 3: Plot the Data

Now, we will plot mu vs. sigma using Matplotlib's pyplot module. We will create a scatter plot using the computed values for mu and sigma. We will also add interactivity to the plot by setting the `picker` parameter to True.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title('click on point to plot time series')
line, = ax.plot(xs, ys, 'o', picker=True, pickradius=5)
```

### Step 4: Add Interactivity

When a point on the scatter plot is clicked, we want to plot the raw data from the dataset that generated that point. We will define a function `onpick` that will be called when a point is clicked. The function will plot the raw data and display the mean and standard deviation for that dataset.

```python
def onpick(event):

    if event.artist != line:
        return

    N = len(event.ind)
    if not N:
        return

    figi, axs = plt.subplots(N, squeeze=False)
    for ax, dataind in zip(axs.flat, event.ind):
        ax.plot(X[dataind])
        ax.text(.05, .9, f'mu={xs[dataind]:1.3f}\nsigma={ys[dataind]:1.3f}',
                transform=ax.transAxes, va='top')
        ax.set_ylim(-0.5, 1.5)
    figi.show()


fig.canvas.mpl_connect('pick_event', onpick)
```

### Step 5: Display the Plot

Finally, we will display the plot using the `show` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to use Matplotlib to compute the mean and standard deviation of 100 datasets and plot mu vs. sigma. We also added interactivity to the plot so that when a point is clicked, the raw data from the dataset that generated that point is displayed. This lab demonstrates the power and flexibility of Matplotlib for exploring and visualizing data.
