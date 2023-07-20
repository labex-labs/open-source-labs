# Remove Tick Labels

We can remove tick labels from a specific subplot by altering the visibility of the labels using the `ax.get_xticklabels()` method. In this example, we will remove the tick labels on the x-axis of the second subplot.

```python
plt.tick_params('x', labelbottom=False)
```
