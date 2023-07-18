# Python Matplotlib Tutorial Lab

## Introduction

Matplotlib is a powerful data visualization library in Python. It is used to create high-quality graphs, charts, and figures for data analysis. In this lab, we will learn how to adjust figure size in different units using Matplotlib.

## Steps

### Step 1: Set Up Environment

Before we start, we need to set up our environment by installing Matplotlib. You can install it using pip in your terminal or command prompt.

```python
!pip install matplotlib
```

We also need to import Matplotlib in our code.

```python
import matplotlib.pyplot as plt
```

### Step 2: Figure Size in Inches (Default)

The default figure size unit in Matplotlib is inches. We can specify the figure size using the figsize parameter in the subplots function. The code below shows how to create a figure with a size of 6 inches x 2 inches.

```python
plt.subplots(figsize=(6, 2))
plt.show()
```

### Step 3: Figure Size in Centimeters

We can also specify the figure size in centimeters. To do this, we need to convert the centimeter-based numbers to inches. We can do this by multiplying the centimeter value with the conversion factor from cm to inches, which is 1/2.54. We can then use this value as the figsize parameter in the subplots function. The code below shows how to create a figure with a size of 15 cm x 5 cm.

```python
cm = 1/2.54  # centimeters in inches
plt.subplots(figsize=(15*cm, 5*cm))
plt.show()
```

### Step 4: Figure Size in Pixel

We can also specify the figure size in pixels. To do this, we need to convert the pixel value to inches. We can get the conversion factor from pixels to inches by dividing 1 by the dpi (dots per inch) value. We can then use this value as the figsize parameter in the subplots function. The code below shows how to create a figure with a size of 600 pixels x 200 pixels.

```python
px = 1/plt.rcParams['figure.dpi']  # pixel in inches
plt.subplots(figsize=(600*px, 200*px))
plt.show()
```

### Step 5: Quick Interactive Work

For quick interactive work, pixels are usually a good size of unit. We can use the default dpi value of 100 to convert pixel values to inches. We can then use this value as the figsize parameter in the subplots function. The code below shows how to create a figure with a size of 6 inches x 2 inches using pixel values.

```python
plt.subplots(figsize=(600/100, 200/100))
plt.show()
```

## Summary

In this lab, we learned how to adjust figure size in different units using Matplotlib. We can specify the figure size in inches, centimeters, or pixels. By default, the figure size unit in Matplotlib is inches. We can convert centimeter-based and pixel values to inches to specify the figure size in these units.
