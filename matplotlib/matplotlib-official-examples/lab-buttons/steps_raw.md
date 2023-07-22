# Lab: Creating a Simple Button GUI to Modify a Sine Wave using Matplotlib

## Introduction

In this lab, you will learn how to create a simple GUI using Matplotlib's `Button` widget. The GUI will allow you to modify a sine wave by changing the frequency using the `Next` and `Previous` buttons.

## Steps

### Step 1: Import the necessary libraries

First, let's import the necessary libraries, including `matplotlib.pyplot`, `numpy`, and `Button` from `matplotlib.widgets`.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
```

### Step 2: Set up the initial plot

Next, we will set up the initial plot. We will create a sine wave with a frequency of 2 Hz using `numpy`'s `arange` function, and plot it using `matplotlib.pyplot`'s `plot` function.

```python
freqs = np.arange(2, 20, 3)
fig, ax = plt.subplots()
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*freqs[0]*t)
l, = ax.plot(t, s, lw=2)
```

### Step 3: Create the button callback functions

Now, we will create two callback functions for the `Next` and `Previous` buttons. These functions will update the plot with a new sine wave with a different frequency.

```python
class Index:
    ind = 0

    def next(self, event):
        self.ind += 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

    def prev(self, event):
        self.ind -= 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

callback = Index()
```

### Step 4: Create the `Next` and `Previous` buttons

Now, we will create the `Next` and `Previous` buttons using `matplotlib.pyplot`'s `add_axes` function, and assign the callback functions we created earlier to them using `on_clicked`.

```python
axprev = fig.add_axes([0.7, 0.05, 0.1, 0.075])
axnext = fig.add_axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)
```

### Step 5: Display the plot

Finally, we will display the plot using `matplotlib.pyplot`'s `show` function.

```python
plt.show()
```

## Summary

In this lab, you learned how to create a simple GUI using Matplotlib's `Button` widget. You learned how to modify a sine wave by changing the frequency using the `Next` and `Previous` buttons.
