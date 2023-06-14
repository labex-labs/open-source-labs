# Matplotlib Tutorial: Creating a Legend with Pre-defined Labels

## Introduction

In data visualization, a legend is a key to interpreting the visual elements of a plot. It helps the viewer to understand the data and the meaning of the visual representation. Matplotlib is a popular Python library for creating data visualizations, including plots with legends. In this tutorial, we will learn how to create a legend with pre-defined labels in Matplotlib.

## Steps

### Step 1: Importing the Required Libraries

We will start by importing the required libraries, which include Matplotlib and NumPy. We use NumPy to generate some fake data for our plot.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generating the Data

Next, we will generate some fake data to use in our plot. We will create two arrays, `a` and `b`, using the NumPy `arange` function. We then calculate two more arrays, `c` and `d`, using the `exp` function to compute the exponential of `a` and `d` as the reverse of `c`.

```python
# Make some fake data.
a = b = np.arange(0, 3, .02)
c = np.exp(a)
d = c[::-1]
```

### Step 3: Creating the Plot

Now we are ready to create our plot. We will use the `plot` function of Matplotlib to plot three lines on the same graph, each with a pre-defined label. We will use the `label` parameter to assign the labels to each line.

```python
# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length')
ax.plot(a, d, 'k:', label='Data length')
ax.plot(a, c + d, 'k', label='Total message length')
```

### Step 4: Adding the Legend

To add the legend to our plot, we use the `legend` function of Matplotlib. We pass in the `loc` parameter to specify the location of the legend, and the `shadow` parameter to add a shadow effect to the legend. We also use the `fontsize` parameter to set the font size of the legend.

```python
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
```

### Step 5: Styling the Legend

Finally, we can style the legend to make it more visually appealing. We use the `get_frame` function to get the frame of the legend, and then use the `set_facecolor` function to set the background color of the frame.

```python
# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('C0')
```

### Step 6: Displaying the Plot

We can now display the plot using the `show` function of Matplotlib.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to create a legend with pre-defined labels in Matplotlib. We used the `plot` function to plot three lines on the same graph, and used the `label` parameter to assign labels to each line. We then used the `legend` function to add the legend to the plot, and styled the legend to make it more visually appealing. By following these steps, you can create legends for your own plots in Matplotlib.
