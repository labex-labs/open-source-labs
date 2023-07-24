# Python Matplotlib Tutorial: Creating Custom Figure Subclasses

## Introduction

In this lab, you will learn how to create custom figure subclasses in Matplotlib. You will create a `WatermarkFigure` class that adds a text watermark to the plot.

## Steps

### Step 1: Import necessary libraries

First, import the necessary libraries: `matplotlib.pyplot` and `numpy`.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a custom figure subclass

Create a custom figure subclass called `WatermarkFigure` that adds a text watermark to the plot. This class inherits from the `Figure` class of Matplotlib.

```python
from matplotlib.figure import Figure

class WatermarkFigure(Figure):
    """A figure with a text watermark."""

    def __init__(self, *args, watermark=None, **kwargs):
        super().__init__(*args, **kwargs)

        if watermark is not None:
            bbox = dict(boxstyle='square', lw=3, ec='gray',
                        fc=(0.9, 0.9, .9, .5), alpha=0.5)
            self.text(0.5, 0.5, watermark,
                      ha='center', va='center', rotation=30,
                      fontsize=40, color='gray', alpha=0.5, bbox=bbox)
```

### Step 3: Create data for the plot

Create some data for the plot. In this example, we will create `x` and `y` arrays using the `numpy` library.

```python
x = np.linspace(-3, 3, 201)
y = np.tanh(x) + 0.1 * np.cos(5 * x)
```

### Step 4: Plot the data using custom figure subclass

Use the `plt.figure()` function to plot the data using the custom figure subclass `WatermarkFigure`. In this example, we will add the watermark text "draft" to the plot.

```python
plt.figure(FigureClass=WatermarkFigure, watermark='draft')
plt.plot(x, y)
```

### Step 5: Review references

Review the references used in this example.

```python
# References
# matplotlib.pyplot.figure
# matplotlib.figure.Figure
# matplotlib.figure.Figure.text
```

## Summary

In this lab, you learned how to create a custom figure subclass in Matplotlib. You created a `WatermarkFigure` class that adds a text watermark to the plot. You also learned how to plot data using the custom figure subclass.
