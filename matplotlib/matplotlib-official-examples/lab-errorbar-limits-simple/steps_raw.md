# Errorbar Limit Selection Lab

## Introduction

In data visualization, it is often necessary to show the degree of uncertainty in the data being plotted. Error bars are a convenient way to represent this uncertainty. In this lab, we will learn how to selectively draw lower and/or upper limit symbols on error bars using the parameters `uplims` and `lolims` in Matplotlib.

## Steps

### Step 1: Import the necessary libraries

In this step, we import the necessary libraries to create our plots.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create the data

In this step, we create the data that we will use to create our error bar plot.

```python
x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)
```

### Step 3: Create the error bar plot with both limits (default)

In this step, we create an error bar plot with both upper and lower limits, which is the default behavior.

```python
plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
```

### Step 4: Create the error bar plot with upper limits only

In this step, we create an error bar plot with only upper limits.

```python
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
```

### Step 5: Create the error bar plot with both upper and lower limits

In this step, we create an error bar plot with both upper and lower limits.

```python
plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True, label='uplims=True, lolims=True')
```

### Step 6: Create the error bar plot with subsets of upper and lower limits

In this step, we create an error bar plot with subsets of upper and lower limits.

```python
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits, label='subsets of uplims and lolims')
```

### Step 7: Create the error bar plot with horizontal error bars

In this step, we create an error bar plot with horizontal error bars.

```python
x = np.arange(10) / 10
y = (x + 0.1)**2

plt.errorbar(x, y, xerr=0.1, xlolims=True, label='xlolims=True')
y = (x + 0.1)**3

plt.errorbar(x + 0.6, y, xerr=0.1, xuplims=upperlimits, xlolims=lowerlimits, label='subsets of xuplims and xlolims')

y = (x + 0.1)**4
plt.errorbar(x + 1.2, y, xerr=0.1, xuplims=True, label='xuplims=True')
```

### Step 8: Add a legend and show the plot

In this step, we add a legend to the plot and display it.

```python
plt.legend(loc='lower right')
plt.show()
```

## Summary

In this lab, we learned how to selectively draw lower and/or upper limit symbols on error bars using the parameters `uplims` and `lolims` in Matplotlib. We also learned how to create error bar plots with horizontal error bars.
