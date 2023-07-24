# Plotting Coherence of Two Signals

## Introduction

This lab demonstrates how to plot the coherence of two signals using Python's Matplotlib library. The coherence of two signals is a measure of their linear relationship, with a value of 1 indicating perfect coherence and a value of 0 indicating no coherence.

## Steps

### Step 1: Import Libraries

The first step is to import the necessary libraries. We will be using NumPy and Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate Signals

Next, we will generate two signals with a coherent part at 10 Hz and a random part. We will also add white noise to the signals.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2
```

### Step 3: Plot Signals

We can now plot the two signals in the time domain using Matplotlib.

```python
fig, axs = plt.subplots(2, 1)
axs[0].plot(t, s1, t, s2)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel('Time')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)
```

### Step 4: Plot Coherence

We can now plot the coherence of the two signals using Matplotlib's `cohere` function.

```python
cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('Coherence')
```

### Step 5: Display Plot

Finally, we can display the plot using Matplotlib's `show` function.

```python
fig.tight_layout()
plt.show()
```

## Summary

This lab demonstrated how to plot the coherence of two signals using Python's Matplotlib library. We generated two signals with a coherent part at 10 Hz and a random part, added white noise to the signals, and plotted the signals in the time domain and their coherence using Matplotlib's `cohere` function.
