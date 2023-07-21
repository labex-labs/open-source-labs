# Creating the Figure and Axes

We will create the figure and axes object using the `subplots()` function. We will also add a yellow circle patch to the axes object using the `patches.Circle()` function.

```python
fig, ax = plt.subplots()
circ = patches.Circle((0.5, 0.5), 0.25, alpha=0.8, fc='yellow')
ax.add_patch(circ)
```
