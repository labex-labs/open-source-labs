# Matplotlib Tutorial Lab

## Introduction

Matplotlib is a popular data visualization library in Python. In this tutorial, you will learn how to connect events that occur when a figure closes. This is useful when you want to perform an action after closing a figure.

## Steps

### Step 1: Import Matplotlib and Define the on_close Function

In this step, we will import Matplotlib and define the `on_close` function that will be called when the figure is closed. The function will simply print a message to the console.

```python
import matplotlib.pyplot as plt

def on_close(event):
    print('Closed Figure!')
```

### Step 2: Create a Figure and Connect the Close Event

In this step, we will create a figure and connect the close event to the `on_close` function defined in Step 1. This is done using the `mpl_connect` method of the figure's canvas.

```python
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close)
```

### Step 3: Add Text to the Figure

In this step, we will add text to the figure to prompt the user to close it. This is done using the `text` method of Matplotlib.

```python
plt.text(0.35, 0.5, 'Close Me!', dict(size=30))
```

### Step 4: Show the Figure

In this step, we will show the figure using the `show` method of Matplotlib.

```python
plt.show()
```

## Summary

In this tutorial, you learned how to connect events that occur when a figure closes using Matplotlib. You can use this to perform an action after closing a figure.
