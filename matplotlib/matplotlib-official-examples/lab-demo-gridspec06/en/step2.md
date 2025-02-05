# Create Data

In this step, we will create some data to plot. We will use the `squiggle_xy` function to generate some sine and cosine waves with different frequencies.

```python
def squiggle_xy(a, b, c, d):
    i = np.arange(0.0, 2*np.pi, 0.05)
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)
```
