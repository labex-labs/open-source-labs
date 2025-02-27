# Построение кривой частичной зависимости для одного признака

В этом шаге мы построим кривые частичной зависимости для одного признака, "возраст", на одной и той же оси. В этом случае `tree_disp.axes_` передается во вторую функцию построения.

```python
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age"])
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age"], ax=tree_disp.axes_, line_kw={"color": "red"}
)
```
