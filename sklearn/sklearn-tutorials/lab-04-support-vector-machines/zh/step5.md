# 使用支持向量机进行回归

- 对于回归问题，可以使用 `SVR` 类来使用支持向量机：

```python
X = [[0, 0], [1, 1]]
y = [0.5, 2.5]
regr = svm.SVR()
regr.fit(X, y)
regr.predict([[1, 1]])
```
