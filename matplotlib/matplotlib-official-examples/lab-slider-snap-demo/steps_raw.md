# Matplotlib Snapping Sliders Lab

## Introduction

In this lab, you will learn how to use Matplotlib to create sliders with discrete values. You will learn how to constrain the values of a slider to a set of allowed values and snap the slider values to those allowed values.

## Steps

### Step 1: Import Required Libraries

In this step, you will import the required libraries for this lab. You will be using Matplotlib to create the sliders and NumPy to generate the data to be plotted.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import Button, Slider
```

### Step 2: Generate Data

In this step, you will generate the data to be plotted. You will create a sine wave with a frequency of 3 Hz and an amplitude of 5.

```python
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
s = a0 * np.sin(2 * np.pi * f0 * t)
```

### Step 3: Create the Figure and Axes

In this step, you will create the figure and axes for the plot. You will also adjust the position of the axes to make room for the sliders.

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.25)
l, = ax.plot(t, s, lw=2)

ax_freq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
ax_amp = fig.add_axes([0.25, 0.15, 0.65, 0.03])
```

### Step 4: Define Allowed Values for the Amplitude Slider

In this step, you will define the allowed values for the amplitude slider. The amplitude slider will use these values to snap to the nearest allowed value.

```python
# define the values to use for snapping
allowed_amplitudes = np.concatenate([np.linspace(.1, 5, 100), [6, 7, 8, 9]])
```

### Step 5: Create the Sliders

In this step, you will create the sliders. You will create one slider for the amplitude and one slider for the frequency.

```python
samp = Slider(
    ax_amp, "Amp", 0.1, 9.0,
    valinit=a0, valstep=allowed_amplitudes,
    color="green"
)

sfreq = Slider(
    ax_freq, "Freq", 0, 10*np.pi,
    valinit=2*np.pi, valstep=np.pi,
    initcolor='none'  # Remove the line marking the valinit position.
)
```

### Step 6: Create the Update Function

In this step, you will create the update function for the sliders. This function will update the plot when the slider values are changed.

```python
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()
```

### Step 7: Connect the Sliders to the Update Function

In this step, you will connect the sliders to the update function. This will ensure that the plot is updated whenever the slider values are changed.

```python
sfreq.on_changed(update)
samp.on_changed(update)
```

### Step 8: Create the Reset Button

In this step, you will create a reset button for the sliders. When clicked, the reset button will reset the slider values to their initial values.

```python
ax_reset = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(ax_reset, 'Reset', hovercolor='0.975')

def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)
```

### Step 9: Show the Plot

In this step, you will show the plot.

```python
plt.show()
```

## Summary

In this lab, you learned how to use Matplotlib to create sliders with discrete values. You learned how to constrain the values of a slider to a set of allowed values and snap the slider values to those allowed values. You also learned how to create a reset button for the sliders.
