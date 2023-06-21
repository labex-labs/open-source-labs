# Annotated Cursor Tutorial

## Introduction

In this lab, we will learn how to create a data cursor including a text box, which shows the plot point close to the mouse pointer using Matplotlib, a plotting library for the Python programming language.

## Steps

### Step 1: Import necessary libraries

We start by importing Matplotlib and NumPy libraries. NumPy is the fundamental package for scientific computing in Python, while Matplotlib is a plotting library that produces publication-quality figures.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a plot

We create a simple plot of a parabola using NumPy's `linspace` function to generate 1000 values between -5 and 5 for x, and then compute y as the square of x.

```python
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Cursor Tracking x Position")

x = np.linspace(-5, 5, 1000)
y = x**2

line, = ax.plot(x, y)
ax.set_xlim(-5, 5)
ax.set_ylim(0, 25)
```

### Step 3: Create the AnnotatedCursor class

We create a new class `AnnotatedCursor` that inherits from `matplotlib.widgets.Cursor` and demonstrates the creation of new widgets and their event callbacks. The `AnnotatedCursor` class is used to create a crosshair cursor with a text showing the current coordinates.

```python
class AnnotatedCursor(Cursor):
    """
    A crosshair cursor like `~matplotlib.widgets.Cursor` with a text showing \
    the current coordinates.
    ...
    """
```

### Step 4: Initialize the AnnotatedCursor object

We initialize the `AnnotatedCursor` object by passing the plot line, `line`, to the `AnnotatedCursor` constructor.

```python
cursor = AnnotatedCursor(line=line, ax=ax, useblit=True)
```

### Step 5: Display the plot

We display the plot using the `show()` method of the Matplotlib `pyplot` module.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a data cursor including a text box, which shows the plot point close to the mouse pointer using Matplotlib. We created a simple plot of a parabola, then created an `AnnotatedCursor` object and displayed the plot.
