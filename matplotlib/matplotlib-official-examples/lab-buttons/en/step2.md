# Set up the initial plot

Next, we will set up the initial plot. We will create a sine wave with a frequency of 2 Hz using `numpy`'s `arange` function, and plot it using `matplotlib.pyplot`'s `plot` function.

```python
freqs = np.arange(2, 20, 3)
fig, ax = plt.subplots()
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*freqs[0]*t)
l, = ax.plot(t, s, lw=2)
```
