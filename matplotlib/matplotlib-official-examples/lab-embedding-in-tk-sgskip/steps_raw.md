# Matplotlib Tutorial Lab

## Introduction

This lab will guide you through embedding a Matplotlib plot into a Tkinter GUI. The GUI will have a slider that allows you to adjust the frequency of a sine wave plotted in real-time.

## Steps

### Step 1: Set up the GUI

We start by creating a Tkinter window and setting its title. We also define the size and resolution of the Matplotlib figure we will use.

```python
import tkinter
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
```

### Step 2: Plot the Sine Wave

We create a sine wave using numpy and plot it on the Matplotlib figure. We also label the x and y axes.

```python
t = np.arange(0, 3, .01)
line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
ax.set_xlabel("time [s]")
ax.set_ylabel("f(t)")
```

### Step 3: Add a Slider

We add a horizontal slider to the GUI that allows the user to adjust the frequency of the sine wave. We also define a function that updates the plot according to the value of the slider.

```python
def update_frequency(new_val):
    # retrieve frequency
    f = float(new_val)

    # update data
    y = 2 * np.sin(2 * np.pi * f * t)
    line.set_data(t, y)

    # required to update canvas and attached toolbar!
    canvas.draw()

slider_update = tkinter.Scale(root, from_=1, to=5, orient=tkinter.HORIZONTAL,
                              command=update_frequency, label="Frequency [Hz]")
```

### Step 4: Add a Toolbar and Quit Button

We add a navigation toolbar that allows the user to zoom in and out of the plot and save it. We also add a button that closes the GUI when clicked.

```python
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

button_quit = tkinter.Button(master=root, text="Quit", command=root.destroy)
```

### Step 5: Pack the Widgets

We pack the widgets into the GUI window. The order in which they are packed is important.

```python
button_quit.pack(side=tkinter.BOTTOM)
slider_update.pack(side=tkinter.BOTTOM)
toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
```

### Step 6: Run the GUI

We run the GUI using the `mainloop()` function of the Tkinter module.

```python
tkinter.mainloop()
```

## Summary

In this lab, we learned how to embed a Matplotlib plot into a Tkinter GUI and add a slider to adjust the plot in real-time. We also added a navigation toolbar and a quit button to the GUI.
