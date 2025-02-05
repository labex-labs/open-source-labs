# Create a Scatter Plot

We will now create a scatter plot using the `plot` function from `matplotlib.pyplot`.

```python
fig = plt.figure(figsize=(5, 10))
ax = plt.subplot(2, 1, 1)

# Plot the data
for x, y in zip(xs, ys):
    plt.plot(x, y, 'ro')
```
