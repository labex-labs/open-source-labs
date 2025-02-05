# 训练模型

现在，我们将借助 `fit()` 方法在鸢尾花数据集上训练 SGDClassifier 模型。此方法将输入数据和目标值作为输入，并在给定数据上训练模型。

```python
clf = SGDClassifier(alpha=0.001, max_iter=100).fit(X, y)
```
