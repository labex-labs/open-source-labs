# Set up variables

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
