# Spectrogram Plotting with Matplotlib: A Step-by-Step Lab

## Introduction

In this lab, we will learn how to create a spectrogram plot using Matplotlib. A spectrogram is a visual representation of the spectrum of frequencies of a signal as it varies with time. Spectrograms are commonly used to analyze the frequency content of a signal over time, such as in speech recognition, music analysis, and audio signal processing. We will use Python and Matplotlib to create a spectrogram plot of a signal.

## Steps

### Step 1: Import Libraries

We will start by importing the necessary libraries: NumPy and Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate Signal

Next, we will generate a signal to plot. In this example, we will create a signal that is the sum of two sine waves with different frequencies, and some random noise.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.0005
t = np.arange(0.0, 20.0, dt)
s1 = np.sin(2 * np.pi * 100 * t)
s2 = 2 * np.sin(2 * np.pi * 400 * t)

# create a transient "chirp"
s2[t <= 10] = s2[12 <= t] = 0

# add some noise into the mix
nse = 0.01 * np.random.random(size=len(t))

x = s1 + s2 + nse  # the signal
```

### Step 3: Generate Spectrogram

Now we will generate a spectrogram plot of the signal. We will use the `specgram` method from Matplotlib's `Axes` class to generate the spectrogram. This method returns four objects: `Pxx`, `freqs`, `bins`, and `im`. `Pxx` is the periodogram, `freqs` is the frequency vector, `bins` is the centers of the time bins, and `im` is the `AxesImage` instance representing the data in the plot.

```python
NFFT = 1024  # the length of the windowing segments
Fs = int(1.0 / dt)  # the sampling frequency

fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.plot(t, x)
Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)
```

### Step 4: Customize Plot

We can customize the plot by adding titles, axis labels, and color maps.

```python
fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.set_title('Time Domain Signal')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')
ax1.plot(t, x)

ax2.set_title('Spectrogram')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Frequency (Hz)')
im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900, cmap='viridis')
fig.colorbar(im[3], ax=ax2)
```

### Step 5: Display Plot

Finally, we will display the plot.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a spectrogram plot using Matplotlib. We generated a signal and used the `specgram` method from Matplotlib's `Axes` class to generate the spectrogram plot. We also customized the plot by adding titles, axis labels, and color maps. Spectrograms are useful for analyzing the frequency content of a signal over time and are commonly used in speech recognition, music analysis, and audio signal processing.
