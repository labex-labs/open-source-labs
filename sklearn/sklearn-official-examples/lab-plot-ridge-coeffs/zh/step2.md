# 生成随机数据

我们将使用 scikit-learn 中的`make_regression`函数生成随机数据。我们将把`n_samples`设置为 10，`n_features`设置为 10，`random_state`设置为 1。此函数将返回我们的输入特征 X、目标变量 y 以及真实系数值 w。

```python
X, y, w = make_regression(
    n_samples=10, n_features=10, coef=True, random_state=1, bias=3.5
)
```
