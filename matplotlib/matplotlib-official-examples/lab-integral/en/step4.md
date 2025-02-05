# Create the plot

Create a figure and axis object using `subplots`. Plot the x and y values using `plot`. Set the y-axis limits to start at 0 using `set_ylim`.

```python
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)
```
