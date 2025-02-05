# 绘制单个特征的局部依赖关系

在这一步中，我们将在同一坐标轴上绘制单个特征“年龄”的局部依赖曲线。在这种情况下，`tree_disp.axes_` 被传递给第二个绘图函数。

```python
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age"])
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age"], ax=tree_disp.axes_, line_kw={"color": "red"}
)
```
