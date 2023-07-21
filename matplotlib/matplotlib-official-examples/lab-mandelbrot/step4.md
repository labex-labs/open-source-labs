# Normalize the Data

In order to create a shaded and power-normalized rendering of the Mandelbrot set, we need to normalize our data. We will do this using the following formula:

`M = N + 1 - np.log2(np.log(abs(Z))) + log_horizon`

```python
with np.errstate(invalid='ignore'):
    M = np.nan_to_num(N + 1 - np.log2(np.log(abs(Z))) + log_horizon)
```
