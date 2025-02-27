# PLS Regression mit eindimensionaler Antwort (PLS1)

Wir verwenden den PLS Regression-Algorithmus mit eindimensionaler Antwort, um die Werte von beta zu schätzen.

```python
n = 1000
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
y = X[:, 0] + 2 * X[:, 1] + np.random.normal(size=n * 1) + 5
pls1 = PLSRegression(n_components=3)
pls1.fit(X, y)
# beachten Sie, dass die Anzahl der Komponenten größer als 1 (die Dimension von y) ist
print("Geschätzte betas")
print(np.round(pls1.coef_, 1))
```
