# Using Radio Buttons to Choose Properties of Your Plot

## Introduction

Radio buttons are a type of input element that allows users to select one option from a group of predefined options. In this lab, we will use the `matplotlib` library to create a visualization with radio buttons that let the user choose between different sine waves to be shown in the plot.

## Steps

### Step 1: Import Required Libraries

We will start by importing the required libraries for this lab - `numpy` and `matplotlib`.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import RadioButtons
```

### Step 2: Create Data

Next, we will create the data that will be used in the plot. We will create three different sine waves with different frequencies using the `numpy` library.

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)
```

### Step 3: Create the Plot and Radio Buttons

Now, we will create the plot and radio buttons. We will use the `subplots()` function to create the plot and the `RadioButtons()` function to create the radio buttons.

```python
fig, ax = plt.subplots()
l, = ax.plot(t, s0, lw=2, color='red')
fig.subplots_adjust(left=0.3)

axcolor = 'lightgoldenrodyellow'
rax = fig.add_axes([0.05, 0.7, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('1 Hz', '2 Hz', '4 Hz'),
                     label_props={'color': 'cmy', 'fontsize': [12, 14, 16]},
                     radio_props={'s': [16, 32, 64]})
```

### Step 4: Add Functionality to the Radio Buttons

We will now add functionality to the radio buttons using the `on_clicked()` function. We will define two functions - `hzfunc()` and `colorfunc()` - that will be called when the radio buttons are clicked.

```python
def hzfunc(label):
    hzdict = {'1 Hz': s0, '2 Hz': s1, '4 Hz': s2}
    ydata = hzdict[label]
    l.set_ydata(ydata)
    fig.canvas.draw()
radio.on_clicked(hzfunc)

rax = fig.add_axes([0.05, 0.4, 0.15, 0.15], facecolor=axcolor)
radio2 = RadioButtons(
    rax, ('red', 'blue', 'green'),
    label_props={'color': ['red', 'blue', 'green']},
    radio_props={
        'facecolor': ['red', 'blue', 'green'],
        'edgecolor': ['darkred', 'darkblue', 'darkgreen'],
    })


def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw()
radio2.on_clicked(colorfunc)

rax = fig.add_axes([0.05, 0.1, 0.15, 0.15], facecolor=axcolor)
radio3 = RadioButtons(rax, ('-', '--', '-.', ':'))


def stylefunc(label):
    l.set_linestyle(label)
    fig.canvas.draw()
radio3.on_clicked(stylefunc)
```

### Step 5: Display the Plot

Finally, we will display the plot using the `show()` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a visualization with radio buttons using the `matplotlib` library. We used radio buttons to let the user choose between different sine waves to be shown in the plot. We also added functionality to the radio buttons by defining functions that were called when the buttons were clicked. Overall, this lab demonstrated how radio buttons can be used to create interactive visualizations that allow users to explore different aspects of the data.
