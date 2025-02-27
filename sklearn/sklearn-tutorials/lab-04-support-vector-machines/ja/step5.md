# SVMによる回帰

- 回帰問題では、SVMを `SVR` クラスとともに使用できます：

```python
X = [[0, 0], [1, 1]]
y = [0.5, 2.5]
regr = svm.SVR()
regr.fit(X, y)
regr.predict([[1, 1]])
```
