# Python Matplotlib Lab

## Introduction

This lab will guide you through the process of using the agg backend directly to create images in Python Matplotlib. The agg backend is useful for web application developers who want full control over their code without using the pyplot interface to manage figures, figure closing, etc. In this lab, we will show you how to save the contents of the agg canvas to a file and how to extract them to a numpy array, which can in turn be passed off to Pillow.

## Steps

### Step 1: Create a Figure and Canvas

First, we need to create a Figure and a Canvas. The Figure defines the size, shape, and content of the plot, while the Canvas is where the Figure is drawn.

```python
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasAgg(fig)
```

### Step 2: Add Plotting Data to the Figure

Now that we have a Figure and a Canvas, we can add some data to the plot. In this example, we will add a simple line plot.

```python
ax = fig.add_subplot()
ax.plot([1, 2, 3])
```

### Step 3: Save the Figure to a File

There are two options for saving the plot. The first option is to save the Figure to a file. In this example, we will save the plot as a PNG image.

```python
fig.savefig("test.png")
```

### Step 4: Extract the Renderer Buffer to a Numpy Array

The second option for saving the plot is to extract the renderer buffer to a numpy array. This allows us to use Matplotlib inside a cgi-script without needing to write a figure to disk. In this example, we will extract the renderer buffer and convert it to a numpy array.

```python
canvas.draw()
rgba = np.asarray(canvas.buffer_rgba())
```

### Step 5: Save the Numpy Array to a Pillow Image

Now that we have the numpy array, we can pass it off to Pillow and save it in any format supported by Pillow. In this example, we will save the plot as a BMP image.

```python
im = Image.fromarray(rgba)
im.save("test.bmp")
```

## Summary

In this lab, we showed you how to use the agg backend in Python Matplotlib to create images. We created a Figure and Canvas, added data to the plot, and saved the plot as a PNG image. We also extracted the renderer buffer to a numpy array and saved the plot as a BMP image using Pillow. These techniques are useful for web application developers who want full control over their code without using the pyplot interface to manage figures, figure closing, etc.
