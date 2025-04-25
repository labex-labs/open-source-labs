# 信号の生成

Matplotlib を使って信号を生成し、可視化します。

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
