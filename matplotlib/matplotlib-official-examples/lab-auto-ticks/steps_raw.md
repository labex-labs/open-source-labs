# Python Matplotlib Tutorial

## Introduction

In this lab, we will learn how to set the behavior of tick auto-placement in Matplotlib. By default, Matplotlib will choose the number of ticks and tick positions so that there is a reasonable number of ticks on the axis and they are located at "round" numbers. However, there may be no ticks on the edges of the plot. We will learn how to switch the `axes.autolimit_mode` to 'round_numbers' to keep ticks at round numbers and also have ticks at the edges.

## Steps

### Step 1: Scatter plot without round_numbers autolimit_mode

In this step, we will create a scatter plot without round_numbers autolimit_mode and observe the behavior of tick auto-placement.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fig, ax = plt.subplots()
dots = np.linspace(0.3, 1.2, 10)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()
ax.scatter(x, y, c=x+y)
plt.show()
```

### Step 2: Scatter plot with round_numbers autolimit_mode

In this step, we will switch `axes.autolimit_mode` to 'round_numbers' and create a scatter plot to keep ticks at round numbers and also have ticks at the edges.

```python
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
plt.show()
```

### Step 3: Scatter plot with additional margin

In this step, we will set an additional margin around the data using `.Axes.set_xmargin` / `.Axes.set_ymargin` while the round numbers autolimit_mode is still respected.

```python
fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
ax.set_xmargin(0.8)
plt.show()
```

## Summary

In this lab, we learned how to set the behavior of tick auto-placement in Matplotlib by switching `axes.autolimit_mode` to 'round_numbers'. We also learned how to set an additional margin around the data while the round numbers autolimit_mode is still respected. These techniques can be used to customize the tick positions on the axis and improve the readability of the plot.
