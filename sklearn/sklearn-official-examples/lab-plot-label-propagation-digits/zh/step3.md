# 训练标签传播模型

我们使用 gamma=0.25 和 max_iter=20 来训练标签传播（Label Spreading）模型。

```python
lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
```
