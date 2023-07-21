# Compute the Cross Spectral Density of Two Signals

## Introduction

In signal processing, Cross Spectral Density (CSD) is a measure of the correlation between two signals in the frequency domain. It is used to determine how much two signals are related to each other in terms of their frequency content. In this lab, you will learn how to compute the CSD of two signals using Python's Matplotlib library.

## Steps

### Step 1: Import Required Libraries

We need to import the following libraries: numpy and matplotlib.pyplot.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate Signals

We need to generate two signals. These signals contain a coherent part and a random part. The coherent part of both signals has a frequency of 10 Hz. The random part of the signals is generated using white noise that is passed through a low-pass filter to create colored noise.

```python
dt = 0.01
t = np.arange(0, 30, dt)

# Fixing random state for reproducibility
np.random.seed(19680801)

nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2
r = np.exp(-t / 0.05)

cnse1 = np.convolve(nse1, r, mode='same') * dt   # colored noise 1
cnse2 = np.convolve(nse2, r, mode='same') * dt   # colored noise 2

# two signals with a coherent part and a random part
s1 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse1
s2 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse2
```

### Step 3: Plot Signals

We can plot the two generated signals using Matplotlib's plot function.

```python
fig, ax = plt.subplots()
ax.plot(t, s1, label='s1')
ax.plot(t, s2, label='s2')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.legend()
plt.show()
```

### Step 4: Compute CSD

To compute the CSD of two signals, we need to use Matplotlib's csd function. The function takes the two signals, the number of points for the FFT, and the sampling frequency as inputs.

```python
fig, ax = plt.subplots()
cxy, f = ax.csd(s1, s2, 256, 1. / dt)
ax.set_ylabel('CSD (dB)')
plt.show()
```

### Step 5: Interpret Results

The resulting plot shows the CSD of the two signals. The x-axis represents the frequency and the y-axis represents the strength of the correlation between the two signals at that frequency. The plot shows a peak at 10 Hz, which is the frequency of the coherent part of the signals. This indicates that the two signals are strongly correlated at this frequency.

## Summary

In this lab, you learned how to compute the Cross Spectral Density of two signals using Python's Matplotlib library. We generated two signals with a coherent part and a random part, plotted the signals, computed the CSD, and interpreted the results. The CSD is a useful tool for determining the correlation between two signals in the frequency domain.
