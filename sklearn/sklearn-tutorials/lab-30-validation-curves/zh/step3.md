# 绘制验证曲线

现在，让我们使用 `validation_curve` 函数绘制验证曲线。我们将使用 `Ridge` 估计器，并在一系列值的范围内改变 `alpha` 超参数。

```python
param_range = np.logspace(-7, 3, 3)
train_scores, valid_scores = validation_curve(
    Ridge(), X, y, param_name="alpha", param_range=param_range, cv=5)
```
