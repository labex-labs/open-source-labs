# Plot a diagonal line

First, we will plot a diagonal line at a 45-degree angle using Matplotlib's `plot()` function.

```python
fig, ax = plt.subplots()

# Plot diagonal line (45 degrees)
h = ax.plot(range(0, 10), range(0, 10))
```
