# Python Matplotlib Lab

## Different Scales on the Same Axes

### Introduction

The purpose of this lab is to demonstrate how to display two scales on the left and right y-axis. This example uses the Fahrenheit and Celsius scales. We will use a closure function to register as a callback to update the second axis according to the first axis.

### Steps

Follow the below steps to create a Python Matplotlib graph with two different scales on the same axes:

### Step 1: Import necessary libraries

First, we need to import the `numpy` and `matplotlib.pyplot` libraries.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define a function to convert Fahrenheit to Celsius

Next, we define a function to convert temperature in Fahrenheit to Celsius.

```python
def fahrenheit2celsius(temp):
    """
    Returns temperature in Celsius given Fahrenheit temperature.
    """
    return (5. / 9.) * (temp - 32)
```

### Step 3: Define a function to update the second axis

We will define a closure function to register as a callback to update the second axis according to the first axis.

```python
def convert_ax_c_to_celsius(ax_f):
    """
    Update second axis according to first axis.
    """
    y1, y2 = ax_f.get_ylim()
    ax_c.set_ylim(fahrenheit2celsius(y1), fahrenheit2celsius(y2))
    ax_c.figure.canvas.draw()
```

### Step 4: Create the plot

Now, we create a plot with two y-axes using the `subplots()` function of `matplotlib.pyplot`. We also connect the `ylim_changed` event of the first axis to the `convert_ax_c_to_celsius()` function.

```python
fig, ax_f = plt.subplots()
ax_c = ax_f.twinx()

ax_f.callbacks.connect("ylim_changed", convert_ax_c_to_celsius)
```

### Step 5: Plot the data

We plot the data using the `plot()` function of the first axis.

```python
ax_f.plot(np.linspace(-40, 120, 100))
```

### Step 6: Set the axis limits and labels

We set the x-axis limits to (0,100), and the y-axis labels and title.

```python
ax_f.set_xlim(0, 100)
ax_f.set_title('Two scales: Fahrenheit and Celsius')
ax_f.set_ylabel('Fahrenheit')
ax_c.set_ylabel('Celsius')
```

### Step 7: Display the plot

Finally, we display the plot using the `show()` function of `matplotlib.pyplot`.

```python
plt.show()
```

### Summary

In this lab, we learned how to display two scales on the left and right y-axis using Python Matplotlib. We used a closure function to register as a callback to update the second axis according to the first axis. This is useful when we want to plot two sets of data with different units.
