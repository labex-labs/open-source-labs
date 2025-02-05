# Compute CSD

To compute the CSD of two signals, we need to use Matplotlib's csd function. The function takes the two signals, the number of points for the FFT, and the sampling frequency as inputs.

```python
fig, ax = plt.subplots()
cxy, f = ax.csd(s1, s2, 256, 1. / dt)
ax.set_ylabel('CSD (dB)')
plt.show()
```
