# 训练模型

现在我们将使用训练数据来训练LOF模型。我们将邻居数量设置为20，将novelty设置为true。我们还将contamination设置为0.1。

```python
clf = LocalOutlierFactor(n_neighbors=20, novelty=True, contamination=0.1)
clf.fit(X_train)
```
