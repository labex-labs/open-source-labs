# Generate a Signal

We will generate a signal and visualize it using Matplotlib.

```python
resolution = 1024
subsampling = 3  # subsampling factor
width = 100
n_components = resolution // subsampling

# Generate a signal
y = np.linspace(0, resolution - 1, resolution)
first_quarter = y < resolution / 4
y[first_quarter] = 3.0
y[np.logical_not(first_quarter)] = -1.0

# Visualize the signal
plt.figure()
plt.plot(y)
plt.title("Original Signal")
plt.show()
```
