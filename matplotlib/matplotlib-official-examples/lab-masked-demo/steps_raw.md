# Python Matplotlib Tutorial: Plotting Masked and NaN Values

## Introduction

In data visualization, it is common to encounter missing data that needs to be plotted. In this tutorial, we will learn how to plot data with missing values using Matplotlib. We will explore three methods: removing undesired data points, masking points, and setting values to NaN.

## Steps

### Step 1: Import the Required Libraries

We need to import the libraries we will be using in this tutorial. We will be using Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create Data for Plotting

We will create data to plot using NumPy. We will generate 31 data points between -pi/2 and pi/2 and calculate the cosine of these values raised to the power of 3.

```python
x = np.linspace(-np.pi/2, np.pi/2, 31)
y = np.cos(x)**3
```

### Step 3: Remove Points

We will remove points where y > 0.7. We will create a new x array and y array with only the remaining points.

```python
x2 = x[y <= 0.7]
y2 = y[y <= 0.7]
```

### Step 4: Mask Points

We will mask points where y > 0.7 using a masked array. We will create a new y array with masked values.

```python
y3 = np.ma.masked_where(y > 0.7, y)
```

### Step 5: Set to NaN

We will set to NaN where y > 0.7. We will create a new y array with NaN values.

```python
y4 = y.copy()
y4[y3 > 0.7] = np.nan
```

### Step 6: Plot the Data

We will plot all four datasets using different markers and colors to differentiate them.

```python
plt.plot(x*0.1, y, 'o-', color='lightgrey', label='No mask')
plt.plot(x2*0.4, y2, 'o-', label='Points removed')
plt.plot(x*0.7, y3, 'o-', label='Masked values')
plt.plot(x*1.0, y4, 'o-', label='NaN values')
plt.legend()
plt.title('Masked and NaN data')
plt.show()
```

### Step 7: Interpret the Plot

The resulting plot will have four lines of different colors and markers. The first line (light grey) represents the original data with no masking. The second line (orange) represents the data with undesired points removed. The third line (green) represents the data with masked values. The fourth line (blue) represents the data with NaN values. This plot shows how missing data can be visualized using different methods.

## Summary

In this tutorial, we learned how to plot data with missing values using Matplotlib. We explored three methods: removing undesired data points, masking points, and setting values to NaN. We created data to plot using NumPy and used different markers and colors to differentiate the datasets. We also interpreted the resulting plot to understand the different methods of visualizing missing data.
