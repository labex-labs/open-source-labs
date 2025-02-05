# 定义 alpha 值

我们将为正则化参数 alpha 定义不同的值。我们将使用 np.logspace 在 0.1 和 10 之间生成 5 个对数间距的值。

```python
alphas = np.logspace(-1, 1, 5)
```
