# Matplotlib Oscilloscope Tutorial

## Introduction

This tutorial is a step-by-step guide on how to create an oscilloscope using Python's Matplotlib library. An oscilloscope is a device used to measure and display voltage signals over time. In this tutorial, we will use Matplotlib's animation module to create a real-time display of a voltage signal.

## Steps

### Step 1: Import Libraries

Before we start coding, we need to import the necessary libraries. We will be using Matplotlib, NumPy, and the animation module.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.lines import Line2D
```

### Step 2: Set up the Scope Class

The Scope class will hold the data and methods we need to create the oscilloscope. In the constructor, we initialize the necessary variables and set up the plot.

```python
class Scope:
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-.1, 1.1)
        self.ax.set_xlim(0, self.maxt)
```

### Step 3: Define the Update Method

The update method is called for each frame of the animation. It takes in a new value and updates the plot accordingly.

```python
def update(self, y):
        lastt = self.tdata[-1]
        if lastt >= self.tdata[0] + self.maxt:  # reset the arrays
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            self.ax.figure.canvas.draw()

        t = self.tdata[0] + len(self.tdata) * self.dt

        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)
        return self.line,
```

### Step 4: Create the Emitter Function

The emitter function generates the data that will be passed to the update method. In this case, we are generating random data with a probability of 0.1.

```python
def emitter(p=0.1):
    while True:
        v = np.random.rand()
        if v > p:
            yield 0.
        else:
            yield np.random.rand()
```

### Step 5: Set up the Plot

We create a new figure and axis object and initialize the Scope class. We then pass the update and emitter functions to the FuncAnimation method to create the animation.

```python
fig, ax = plt.subplots()
scope = Scope(ax)

ani = animation.FuncAnimation(fig, scope.update, emitter, interval=50,
                              blit=True, save_count=100)

plt.show()
```

## Summary

In this tutorial, we learned how to use Matplotlib to create an oscilloscope that displays voltage signals over time. We defined a Scope class to hold the data and methods needed for the oscilloscope, created an update method to update the plot, and used the emitter function to generate the data. Finally, we set up the plot and passed the update and emitter functions to the FuncAnimation method to create the animation.
