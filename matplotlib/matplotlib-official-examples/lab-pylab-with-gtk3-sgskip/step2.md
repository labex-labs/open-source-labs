# Create Figure and Axis

Next, we will create a figure and axis using the `subplots()` method. We will then plot two lines on the axis and add a legend to distinguish them.

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```
