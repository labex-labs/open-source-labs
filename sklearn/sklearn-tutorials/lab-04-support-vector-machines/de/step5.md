# Regression mit SVM

- Für Regressionsprobleme können SVMs mit der Klasse `SVR` verwendet werden:

```python
X = [[0, 0], [1, 1]]
y = [0.5, 2.5]
regr = svm.SVR()
regr.fit(X, y)
regr.predict([[1, 1]])
```
