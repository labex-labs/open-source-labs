# Generate the data

Next, we need to generate the data for the line plot. We will use the `numpy` library to generate an array of values for `r` and `theta`.

```python
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
```
