# Generate Data

In this step, we will generate the data for the line plot. We will be using the NumPy `arange()` function to generate an array of values for the x-axis, and the `sin()` function to generate an array of y-axis values for a sine wave.

```python
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))
```
