# Plotting Partial Dependence for One Feature

In this step, we will plot the partial dependence curves for a single feature, "age", on the same axes. In this case, `tree_disp.axes_` is passed into the second plot function.

```python
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age"])
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age"], ax=tree_disp.axes_, line_kw={"color": "red"}
)
```
