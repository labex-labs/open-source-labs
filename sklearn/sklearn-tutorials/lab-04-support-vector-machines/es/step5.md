# Regresión con SVM

- Para problemas de regresión, se pueden utilizar SVM con la clase `SVR`:

```python
X = [[0, 0], [1, 1]]
y = [0.5, 2.5]
regr = svm.SVR()
regr.fit(X, y)
regr.predict([[1, 1]])
```
