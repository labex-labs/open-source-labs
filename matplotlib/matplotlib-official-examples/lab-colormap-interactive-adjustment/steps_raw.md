# Interactive Colormap Adjustment Lab

## Introduction

In this lab, you will learn how to use Matplotlib to interactively adjust the range of colormapping on an image using a colorbar. You will use the zoom and pan mode to adjust the vmin and vmax of the norm. Zooming using the right mouse button will expand the vmin and vmax proportionally to the selected region. When panning, the vmin and vmax of the norm are both shifted according to the direction of movement. You can also use the Home/Back/Forward buttons to get back to a previous state.

## Steps

### Step 1: Import Required Libraries

To get started with this lab, you need to import the required libraries. In this lab, we will use `matplotlib.pyplot` and `numpy` libraries.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate Data

Next, you will generate some sample data. In this lab, we will generate a two-dimensional sine wave.

```python
t = np.linspace(0, 2 * np.pi, 1024)
data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]
```

### Step 3: Create the Plot

Now that you have generated the data, you will create the plot using `imshow()` function.

```python
fig, ax = plt.subplots()
im = ax.imshow(data2d)
ax.set_title('Pan on the colorbar to shift the color mapping\n'
             'Zoom on the colorbar to scale the color mapping')
```

### Step 4: Add the Colorbar

To interactively adjust the colormap, you need to add a colorbar to the plot using `colorbar()` function.

```python
fig.colorbar(im, ax=ax, label='Interactive colorbar')
```

### Step 5: Adjust the Colormap

Now, you can interactively adjust the range of colormapping on the image using the colorbar. You can zoom or pan by clicking inside the colorbar. When zooming, the bounding box of the zoom region defines the new vmin and vmax of the norm. Zooming using the right mouse button will expand the vmin and vmax proportionally to the selected region. When panning, the vmin and vmax of the norm are both shifted according to the direction of movement.

### Step 6: Display the Plot

Finally, you can display the plot using `show()` function.

```python
plt.show()
```

## Summary

In this lab, you learned how to use Matplotlib to interactively adjust the range of colormapping on an image using a colorbar. You used the zoom and pan mode to adjust the vmin and vmax of the norm. Zooming using the right mouse button expanded the vmin and vmax proportionally to the selected region. When panning, the vmin and vmax of the norm were both shifted according to the direction of movement. You also learned how to add a colorbar to the plot and display the plot.
