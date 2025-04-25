# 训练模型

现在我们将使用训练数据来训练 LOF 模型。我们将邻居数量设置为 20，将 novelty 设置为 true。我们还将 contamination 设置为 0.1。

```python
clf = LocalOutlierFactor(n_neighbors=20, novelty=True, contamination=0.1)
clf.fit(X_train)
```
