# Set up Plot

Now, we can set up the plot. We will use `plt.subplots()` to create a figure and axis object. Then, we will use `ax.triplot()` to plot the triangulation.

```python
fig, ax = plt.subplots()
ax.triplot(triang)
```
