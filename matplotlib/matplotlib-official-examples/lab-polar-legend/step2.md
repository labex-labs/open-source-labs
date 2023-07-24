# Create a Figure and Subplot

Next, we need to create a figure and subplot for our plot. We will be using the `projection` parameter of `add_subplot` to create a polar plot.

```python
fig = plt.figure()
ax = fig.add_subplot(projection="polar", facecolor="lightgoldenrodyellow")
```
