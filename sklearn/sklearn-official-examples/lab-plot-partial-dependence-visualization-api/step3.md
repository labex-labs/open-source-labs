# Plotting Partial Dependence of the Two Models Together

In this step, we will plot the partial dependence curves of the two models on the same plot.

```python
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
tree_disp.plot(ax=ax1)
ax1.set_title("Decision Tree")
mlp_disp.plot(ax=ax2, line_kw={"color": "red"})
ax2.set_title("Multi-layer Perceptron")
```

Another way to compare the curves is to plot them on top of each other. Here, we create a figure with one row and two columns. The axes are passed into the `PartialDependenceDisplay.plot` function as a list, which will plot the partial dependence curves of each model on the same axes. The length of the axes list must be equal to the number of plots drawn.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
tree_disp.plot(ax=[ax1, ax2], line_kw={"label": "Decision Tree"})
mlp_disp.plot(
    ax=[ax1, ax2], line_kw={"label": "Multi-layer Perceptron", "color": "red"}
)
ax1.legend()
ax2.legend()
```

`tree_disp.axes_` is a numpy array container the axes used to draw the partial dependence plots. This can be passed to `mlp_disp` to have the same affect of drawing the plots on top of each other. Furthermore, the `mlp_disp.figure_` stores the figure, which allows for resizing the figure after calling `plot`. In this case `tree_disp.axes_` has two dimensions, thus `plot` will only show the y label and y ticks on the left most plot.

```python
tree_disp.plot(line_kw={"label": "Decision Tree"})
mlp_disp.plot(
    line_kw={"label": "Multi-layer Perceptron", "color": "red"}, ax=tree_disp.axes_
)
tree_disp.figure_.set_size_inches(10, 6)
tree_disp.axes_[0, 0].legend()
tree_disp.axes_[0, 1].legend()
plt.show()
```
