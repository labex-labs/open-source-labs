# Create a histogram

In this step, we will create a histogram using matplotlib. We will set the number of bins to 50 and enable the density parameter to normalize bin heights so that the integral of the histogram is 1.

```python
num_bins = 50
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=True)
```
