# Generate Spectrogram

Now we will generate a spectrogram plot of the signal. We will use the `specgram` method from Matplotlib's `Axes` class to generate the spectrogram. This method returns four objects: `Pxx`, `freqs`, `bins`, and `im`. `Pxx` is the periodogram, `freqs` is the frequency vector, `bins` is the centers of the time bins, and `im` is the `AxesImage` instance representing the data in the plot.

```python
NFFT = 1024  # the length of the windowing segments
Fs = int(1.0 / dt)  # the sampling frequency

fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.plot(t, x)
Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)
```
