# Plotting Partial Dependence for Two Features

In this step, we will plot partial dependence curves for features "age" and "bmi" (body mass index) for the decision tree. With two features, `PartialDependenceDisplay.from_estimator` expects to plot two curves. Here the plot function place a grid of two plots using the space defined by `ax`.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Decision Tree")
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age", "bmi"], ax=ax)
```

The partial dependence curves can be plotted for the multi-layer perceptron. In this case, `line_kw` is passed to `PartialDependenceDisplay.from_estimator` to change the color of the curve.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Multi-layer Perceptron")
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age", "bmi"], ax=ax, line_kw={"color": "red"}
)
```


