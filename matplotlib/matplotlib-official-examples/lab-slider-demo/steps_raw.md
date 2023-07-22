# Python Matplotlib Slider Tutorial

## Introduction

In this tutorial, we will learn how to create sliders and use them to control a sine wave's frequency and amplitude. We will use the Matplotlib library to create a graph of the sine wave and the sliders. The sliders will allow us to adjust the frequency and amplitude of the sine wave.

## Steps

### Step 1: Import Libraries

The first step is to import the necessary libraries. We will be using Matplotlib and NumPy.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider
```

### Step 2: Define the Sine Wave Function

Next, we will define the function that will generate our sine wave. The function will take in two parameters, amplitude and frequency, and return the sine wave at a given time.

```python
def f(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)
```

### Step 3: Create the Initial Graph

Now, we will create the initial graph of the sine wave. We will define the initial parameters for the amplitude and frequency and plot the sine wave using those parameters.

```python
t = np.linspace(0, 1, 1000)
init_amplitude = 5
init_frequency = 3

fig, ax = plt.subplots()
line, = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
ax.set_xlabel('Time [s]')
```

### Step 4: Create the Sliders

We will now create the sliders that will allow us to adjust the frequency and amplitude of the sine wave. We will create a horizontal slider to control the frequency and a vertical slider to control the amplitude.

```python
fig.subplots_adjust(left=0.25, bottom=0.25)
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label='Frequency [Hz]',
    valmin=0.1,
    valmax=30,
    valinit=init_frequency,
)

axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(
    ax=axamp,
    label="Amplitude",
    valmin=0,
    valmax=10,
    valinit=init_amplitude,
    orientation="vertical"
)
```

### Step 5: Create the Update Function

We will now create the function that will update the sine wave every time we adjust the sliders. The function will take in the values of the amplitude and frequency sliders, and update the sine wave accordingly.

```python
def update(val):
    line.set_ydata(f(t, amp_slider.val, freq_slider.val))
    fig.canvas.draw_idle()
```

### Step 6: Register the Update Function with the Sliders

Next, we will register the update function with each slider so that the function is called every time we adjust the sliders.

```python
freq_slider.on_changed(update)
amp_slider.on_changed(update)
```

### Step 7: Create the Reset Button

We will now create a reset button that will reset the sliders to their initial values.

```python
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    freq_slider.reset()
    amp_slider.reset()
button.on_clicked(reset)
```

### Step 8: Show the Graph

Finally, we will show the graph with the sliders and the reset button.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to create sliders and use them to control a sine wave's frequency and amplitude. We used the Matplotlib library to create a graph of the sine wave and the sliders. We created a horizontal slider to control the frequency and a vertical slider to control the amplitude. We also created a reset button that reset the sliders to their initial values.
