# Generate Data

In this step, you will generate the data to be plotted. You will create a sine wave with a frequency of 3 Hz and an amplitude of 5.

```python
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
s = a0 * np.sin(2 * np.pi * f0 * t)
```
