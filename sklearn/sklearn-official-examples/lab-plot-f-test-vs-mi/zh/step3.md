# 计算 F 检验

现在我们将计算每个特征的 F 检验分数。F 检验仅捕捉变量之间的线性相关性。我们将通过将 F 检验分数除以最大 F 检验分数来对其进行归一化。

```python
f_test, _ = f_regression(X, y)
f_test /= np.max(f_test)
```
