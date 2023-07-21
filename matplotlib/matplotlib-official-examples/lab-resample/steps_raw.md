# **Resampling Data using Matplotlib**

## Introduction

In this lab, we will learn how to downsample data using Matplotlib in Python. Downsampling is the process of reducing the sample rate or sample size of a signal. We will use a class that will downsample the data and recompute when zoomed.

## Steps

### Step 1: Importing libraries

We will start by importing the necessary libraries. We will be using Matplotlib and NumPy libraries for this task.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Defining the class

We will define a class `DataDisplayDownsampler` that will downsample the data and recompute when zoomed. The constructor of the class will take the xdata and ydata as input parameters. We will set the maximum number of points to 50 and calculate the delta of xdata.

```python
class DataDisplayDownsampler:
    def __init__(self, xdata, ydata):
        self.origYData = ydata
        self.origXData = xdata
        self.max_points = 50
        self.delta = xdata[-1] - xdata[0]
```

### Step 3: Downsampling data

We will define a method `downsample` that will downsample the data. The method will take the xstart and xend as input parameters. We will get the points in the view range and dilate the mask by one to catch the points just outside of the view range to not truncate the line. We will sort out how many points to drop and mask the data. Finally, we will downsample the data and return the xdata and ydata.

```python
def downsample(self, xstart, xend):
    # get the points in the view range
    mask = (self.origXData > xstart) & (self.origXData < xend)
    # dilate the mask by one to catch the points just outside
    # of the view range to not truncate the line
    mask = np.convolve([1, 1, 1], mask, mode='same').astype(bool)
    # sort out how many points to drop
    ratio = max(np.sum(mask) // self.max_points, 1)

    # mask data
    xdata = self.origXData[mask]
    ydata = self.origYData[mask]

    # downsample data
    xdata = xdata[::ratio]
    ydata = ydata[::ratio]

    print(f"using {len(ydata)} of {np.sum(mask)} visible points")

    return xdata, ydata
```

### Step 4: Updating the data

We will define a method `update` that will update the data. The method will take the ax (axis) as an input parameter. We will update the line by getting the view limit and checking if the width of the view limit is different from delta. If the width of the view limit is different from delta, we will update the delta and get the xstart and xend. We will then set the data to the downsampled data and draw the idle.

```python
def update(self, ax):
    # Update the line
    lims = ax.viewLim
    if abs(lims.width - self.delta) > 1e-8:
        self.delta = lims.width
        xstart, xend = lims.intervalx
        self.line.set_data(*self.downsample(xstart, xend))
        ax.figure.canvas.draw_idle()
```

### Step 5: Creating the signal

We will create a signal using NumPy. We will create an array xdata using linspace function with start=16, stop=365 and num= (365-16)\*4. We will create an array ydata using sin and cos functions.

```python
xdata = np.linspace(16, 365, (365-16)*4)
ydata = np.sin(2*np.pi*xdata/153) + np.cos(2*np.pi*xdata/127)
```

### Step 6: Creating the plot

We will create a plot using Matplotlib. We will create an instance `d` of the `DataDisplayDownsampler` class using xdata and ydata. We will create a figure and an axis using subplots function. We will hook up the line and set the autoscale on False. We will connect for changing the view limits, set the x limit and show the plot.

```python
d = DataDisplayDownsampler(xdata, ydata)
fig, ax = plt.subplots()
d.line, = ax.plot(xdata, ydata, 'o-')
ax.set_autoscale_on(False)
ax.callbacks.connect('xlim_changed', d.update)
ax.set_xlim(16, 365)
plt.show()
```

## Summary

In this lab, we learned how to downsample data using Matplotlib in Python. We used a class that downsamples the data and recomputes when zoomed. We created a signal using NumPy and created a plot using Matplotlib. We connected for changing the view limits and set the x limit.
