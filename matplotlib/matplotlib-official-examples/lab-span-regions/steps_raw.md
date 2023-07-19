# Matplotlib Tutorial: Shade Regions with fill_between

## Introduction

In this lab, we will learn how to shade regions in a Matplotlib plot using the `fill_between` function. This is useful for highlighting specific areas of the plot, such as regions where a certain condition is met.

## Steps

### Step 1: Import Necessary Libraries

We will start by importing the necessary libraries for this lab, which are `numpy` and `matplotlib.pyplot`.

```python
import numpy as np
import matplotlib.pyplot as plt
```

### Step 2: Create Data

We will create some data to use for our plot. In this example, we will create a sine wave.

```python
t = np.arange(0.0, 2, 0.01)
s = np.sin(2*np.pi*t)
```

### Step 3: Create the Plot

Now we will create the plot using `matplotlib.pyplot`. We will plot the sine wave and add a horizontal line at y=0.

```python
fig, ax = plt.subplots()

ax.plot(t, s, color='black')
ax.axhline(0, color='black')
```

### Step 4: Shade the Regions

We will use `fill_between` to shade the regions above and below the horizontal line where the sine wave is positive and negative, respectively.

```python
ax.fill_between(t, 1, where=s > 0, facecolor='green', alpha=.5)
ax.fill_between(t, -1, where=s < 0, facecolor='red', alpha=.5)
```

### Step 5: Show the Plot

Finally, we will show the plot using `plt.show()`.

```python
plt.show()
```

## Summary

In this lab, we learned how to shade regions in a Matplotlib plot using the `fill_between` function. This is a useful tool for highlighting specific areas of the plot. We hope you found this lab helpful!
