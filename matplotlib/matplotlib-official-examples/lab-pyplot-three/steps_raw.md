# Matplotlib Tutorial: Plotting Multiple Datasets

## Introduction

Matplotlib is a popular data visualization library in Python. In this lab, you will learn how to plot multiple datasets using a single call to the `plot` function in Matplotlib.

## Steps

### Step 1: Import the Required Libraries

In this step, we will import the necessary libraries, including `numpy` and `matplotlib`. We will also set up Matplotlib to display plots inline within the Jupyter Notebook.

```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
```

### Step 2: Create the Data

In this step, we will create three different datasets using the `arange` function from NumPy. We will create a time series with 200ms intervals, ranging from 0 to 5 seconds.

```python
t = np.arange(0., 5., 0.2)
```

### Step 3: Plot the Data

In this step, we will use the `plot` function in Matplotlib to plot all three datasets in a single call. We will use red dashes for the first dataset, blue squares for the second dataset, and green triangles for the third dataset.

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.show()
```

### Step 4: Add Labels and Titles

In this step, we will add a title to the plot and label the x and y axes.

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.title("Multiple Datasets")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.show()
```

## Summary

In this lab, you learned how to plot multiple datasets using a single call to the `plot` function in Matplotlib. You also learned how to add labels and titles to the plot to make it more informative. Matplotlib is a powerful library that offers many options for customizing plots and visualizations.
