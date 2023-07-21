# Python Matplotlib Tutorial

## Introduction

This tutorial will guide you through the process of creating text and arrow annotations using a centimeter-scale plot in Python Matplotlib.

## Steps

### Step 1: Import necessary libraries and define units

In this step, we will import the necessary libraries and define the unit of measurement that we will be using for our plot.

```python
from basic_units import cm
import matplotlib.pyplot as plt
```

### Step 2: Create a plot

In this step, we will create a plot using the `subplots()` function and store it in the `fig` and `ax` variables.

```python
fig, ax = plt.subplots()
```

### Step 3: Add text annotation

In this step, we will add a text annotation to the plot using the `annotate()` function. We will provide the position of the annotation and the text to be displayed.

```python
ax.annotate("Note 01", [0.5*cm, 0.5*cm])
```

### Step 4: Add arrow annotation with unitized xy and text

In this step, we will add an arrow annotation to the plot using the `annotate()` function. We will provide the position of the arrow, the text to be displayed, and the arrow properties. We will also specify the units of measurement for the position and text.

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8*cm, 0.95*cm), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```

### Step 5: Add arrow annotation with mixed units

In this step, we will add another arrow annotation to the plot using the `annotate()` function. We will provide the position of the arrow, the text to be displayed, and the arrow properties. We will also mix units of measurement for the position and use the axes fraction for the text.

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```

### Step 6: Set plot limits and display the plot

In this step, we will set the limits of the plot and display it using the `set_xlim()`, `set_ylim()`, and `show()` functions.

```python
ax.set_xlim(0*cm, 4*cm)
ax.set_ylim(0*cm, 4*cm)
plt.show()
```

## Summary

This tutorial demonstrated how to create text and arrow annotations using a centimeter-scale plot in Python Matplotlib. We imported necessary libraries, defined units, created a plot, added text and arrow annotations, set plot limits, and displayed the plot.
