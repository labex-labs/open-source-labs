# Generate Data

Next, you will generate some sample data. In this lab, we will generate a two-dimensional sine wave.

```python
t = np.linspace(0, 2 * np.pi, 1024)
data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]
```
