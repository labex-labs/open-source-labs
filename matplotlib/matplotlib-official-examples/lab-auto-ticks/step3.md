# Scatter plot with additional margin

In this step, we will set an additional margin around the data using `.Axes.set_xmargin` / `.Axes.set_ymargin` while the round numbers autolimit_mode is still respected.

```python
fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
ax.set_xmargin(0.8)
plt.show()
```
