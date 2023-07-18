# Spectrum Representations Lab

## Introduction

This lab will guide you through generating and visualizing a sine signal with additive noise using Python's Matplotlib library. Specifically, we will create different spectrum representations of the signal using the fast Fourier transform (FFT).

## Steps

### Step 1: Import necessary libraries

First, we need to import the necessary libraries. We will be using NumPy and Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Set up variables

Next, we will set up the variables for our signal. We will use a sampling interval of 0.01, which gives us a sampling frequency of 100 Hz. We will create a time array from 0 to 10 seconds with a step of 0.01 seconds. We will also generate noise using NumPy's `randn` function and convolve it with an exponential decay function to create a noisy signal.

```python
np.random.seed(0)

dt = 0.01  # sampling interval
Fs = 1 / dt  # sampling frequency
t = np.arange(0, 10, dt)

# generate noise:
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)
cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]

s = 0.1 * np.sin(4 * np.pi * t) + cnse  # the signal
```

### Step 3: Create plots

Now we will create the plots for our different spectrum representations. We will use Matplotlib's `subplots` function to create a 3x2 grid of plots. We will plot the time signal in the first plot and the different spectrum types in the remaining plots.

```python
fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(7, 7))

# plot time signal:
axs[0, 0].set_title("Signal")
axs[0, 0].plot(t, s, color='C0')
axs[0, 0].set_xlabel("Time")
axs[0, 0].set_ylabel("Amplitude")

# plot different spectrum types:
axs[1, 0].set_title("Magnitude Spectrum")
axs[1, 0].magnitude_spectrum(s, Fs=Fs, color='C1')

axs[1, 1].set_title("Log. Magnitude Spectrum")
axs[1, 1].magnitude_spectrum(s, Fs=Fs, scale='dB', color='C1')

axs[2, 0].set_title("Phase Spectrum ")
axs[2, 0].phase_spectrum(s, Fs=Fs, color='C2')

axs[2, 1].set_title("Angle Spectrum")
axs[2, 1].angle_spectrum(s, Fs=Fs, color='C2')

axs[0, 1].remove()  # don't display empty ax

fig.tight_layout()
plt.show()
```

### Step 4: Interpret plots

We can see that the first plot shows the signal in the time domain. The second plot shows the magnitude spectrum of the signal, which tells us the strength of the different frequency components in the signal. The third plot shows the logarithmic magnitude spectrum, which is useful for visualizing the entire spectrum when there are very large and very small values. The fourth plot shows the phase spectrum, which tells us the phase shift of each frequency component in the signal. Finally, the fifth plot shows the angle spectrum, which is similar to the phase spectrum but uses radians instead of degrees.

## Summary

In this lab, we generated a sine signal with additive noise and created different spectrum representations of the signal using Python's Matplotlib library. We learned how to interpret the different spectrum types and how they can be useful in analyzing signals.
