# Stem Plot

## Introduction

The stem plot is a type of plot used in data visualization. It is used to plot vertical lines from a baseline to the y-coordinate and places a marker at the tip. In this lab, we will learn how to use the stem plot function in Python's Matplotlib library.

## Steps

### Step 1: Import Libraries

Before we begin, we need to import the necessary libraries. In this case, we will be using the Matplotlib and Numpy libraries.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate Data

Next, we need to generate some data to use in our stem plot. We will create two arrays using the Numpy library.

```python
x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))
```

### Step 3: Create a Basic Stem Plot

We can now create a basic stem plot using the `stem` function from the Matplotlib library.

```python
plt.stem(x, y)
plt.show()
```

This will generate a plot with vertical lines from the baseline to the y-coordinate and markers at the tip.

### Step 4: Customizing the Plot

We can customize the plot by adjusting the baseline using the `bottom` parameter. We can also adjust the format properties of the plot using the `linefmt`, `markerfmt`, and `basefmt` parameters.

```python
markerline, stemlines, baseline = plt.stem(
    x, y, linefmt='grey', markerfmt='D', bottom=1.1)
markerline.set_markerfacecolor('none')
plt.show()
```

This will generate a plot with a grey line format and diamond-shaped markers. The baseline has also been adjusted to 1.1.

### Summary

In this lab, we learned how to use the stem plot function in Python's Matplotlib library. We first imported the necessary libraries, generated some data, and created a basic stem plot. We then customized the plot by adjusting the baseline and format properties. By following these steps, we can create informative and visually appealing stem plots for our data.
