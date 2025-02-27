# Régression avec SVM

- Pour les problèmes de régression, les SVM peuvent être utilisés avec la classe `SVR` :

```python
X = [[0, 0], [1, 1]]
y = [0.5, 2.5]
regr = svm.SVR()
regr.fit(X, y)
regr.predict([[1, 1]])
```
