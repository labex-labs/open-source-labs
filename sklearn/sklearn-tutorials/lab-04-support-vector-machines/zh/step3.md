# 分数和概率

- 支持向量机（SVM）并不直接提供概率估计，但你可以通过将 `probability` 参数设置为 `True` 来启用概率估计：

```python
clf = svm.SVC(probability=True)
clf.fit(X, y)
```

- 然后你可以使用 `predict_proba` 方法来获取每个类别的概率：

```python
clf.predict_proba([[2., 2.]])
```

- 请注意，概率估计计算成本较高且需要进行交叉验证，所以要谨慎使用。
