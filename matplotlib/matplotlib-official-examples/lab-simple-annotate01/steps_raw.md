# Simple Matplotlib Annotation Lab

## Introduction

This lab will guide you through the process of adding annotations to your Matplotlib plots. Annotations help to highlight specific data points or provide additional information to the viewer. The annotations can include text, arrows, and shapes. You will learn how to add annotations to your plot, customize them, and position them.

## Steps

### Step 1: Import Matplotlib

Before we can begin working with Matplotlib, we need to import it. The following code will import Matplotlib and allow us to use its plotting functions.

```python
import matplotlib.pyplot as plt
```

### Step 2: Create a Plot

We will now create a plot to annotate. The following code will create a plot with two data points.

```python
fig, ax = plt.subplots()
x = [1, 2]
y = [3, 4]
ax.plot(x, y, "o")
```

### Step 3: Add Text Annotation

We will now add a text annotation to the plot. The following code will add the text "Data Point 1" at the first data point.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05))
```

### Step 4: Add Arrow Annotation

We will now add an arrow annotation to the plot. The following code will add an arrow from the first data point to the second data point.

```python
ax.annotate("", xy=(1, 3), xytext=(2, 4),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
```

### Step 5: Add Shape Annotation

We will now add a shape annotation to the plot. The following code will add a rectangle around the second data point.

```python
bbox = dict(boxstyle="round", fc="0.8")
ax.annotate("Data Point 2", xy=(2, 4), xytext=(2.5, 4.5),
            bbox=bbox,
            arrowprops=dict(facecolor="black", shrink=0.05))
```

### Step 6: Customize Annotations

We can customize the annotations by changing the font size, font color, and arrow style. The following code will change the font size, font color, and arrow style of the text annotation.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05, arrowstyle="->"),
            fontsize=12, color="red")
```

### Step 7: Position Annotations

We can position the annotations using different coordinate systems. The following code will position the text annotation using data coordinates and the arrow annotation using figure coordinates.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="data")
ax.annotate("", xy=(1, 3), xytext=(0.5, 0.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="figure fraction")
```

## Summary

In this lab, you learned how to add annotations to your Matplotlib plots. You learned how to add text, arrow, and shape annotations, customize them, and position them. Annotations help to highlight specific data points or provide additional information to the viewer.
