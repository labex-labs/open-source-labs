# 绘制两个特征的局部依赖关系

在这一步中，我们将为决策树绘制特征“年龄”和“体重指数”（BMI）的局部依赖曲线。对于两个特征，`PartialDependenceDisplay.from_estimator` 期望绘制两条曲线。这里的绘图函数使用 `ax` 定义的空间放置一个包含两个子图的网格。

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Decision Tree")
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age", "bmi"], ax=ax)
```

也可以为多层感知器绘制局部依赖曲线。在这种情况下，将 `line_kw` 传递给 `PartialDependenceDisplay.from_estimator` 以更改曲线的颜色。

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Multi-layer Perceptron")
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age", "bmi"], ax=ax, line_kw={"color": "red"}
)
```
