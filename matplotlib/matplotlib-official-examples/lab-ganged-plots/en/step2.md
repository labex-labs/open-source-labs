# Generate Data

We generate some sample data to be plotted. Here, we use the `numpy` library to generate three arrays of data.

```python
t = np.arange(0.0, 2.0, 0.01)

s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = s1 * s2
```
