# Customize the plot

To customize the plot, we can use the following methods:

- `set_rmax` to set the maximum value for `r`
- `set_rticks` to set the tick values for `r`
- `set_rlabel_position` to set the position of the radial labels

```python
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.set_rlabel_position(-22.5)
```

We can also add a title to the plot using the `set_title` method.

```python
ax.set_title("A line plot on a polar axis", va='bottom')
```

Finally, we can add a grid to the plot using the `grid` method.

```python
ax.grid(True)
```
