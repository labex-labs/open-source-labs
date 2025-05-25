# Regressão com SVM

- Para problemas de regressão, as máquinas de vetores de suporte (SVMs) podem ser usadas com a classe `SVR`:

```python
X = [[0, 0], [1, 1]]
y = [0.5, 2.5]
regr = svm.SVR()
regr.fit(X, y)
regr.predict([[1, 1]])
```
