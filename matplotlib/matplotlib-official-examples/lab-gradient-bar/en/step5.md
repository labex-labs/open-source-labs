# Create the plot

Now, we can create the plot. We will first create a figure and an axes object. We will then set the x and y limits of the axes. We will create a gradient background using the `gradient_image()` function. Finally, we will create a random data set and use the `gradient_bar()` function to create the bar chart.

```python
fig, ax = plt.subplots()
ax.set(xlim=(0, 10), ylim=(0, 1))

# background image
gradient_image(ax, direction=1, extent=(0, 1, 0, 1), transform=ax.transAxes,
               cmap=plt.cm.RdYlGn, cmap_range=(0.2, 0.8), alpha=0.5)

N = 10
x = np.arange(N) + 0.15
y = np.random.rand(N)
gradient_bar(ax, x, y, width=0.7)
plt.show()
```
