# 使用标签传播学习标签

我们使用“标签传播”（LabelSpreading）来学习未知样本的标签。

```python
label_spread = LabelSpreading(kernel="knn", alpha=0.8)
label_spread.fit(X, labels)
```
