# PLS Regression mit multivariater Antwort (PLS2)

Wir verwenden den PLS Regression-Algorithmus mit multivariater Antwort, um die Werte einer Matrix B zu schätzen. Anschließend vergleichen wir die geschätzte B mit der wahren B.

```python
n = 1000
q = 3
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
B = np.array([[1, 2] + [0] * (p - 2)] * q).T
# jeder Yj = 1*X1 + 2*X2 + Rauschen
Y = np.dot(X, B) + np.random.normal(size=n * q).reshape((n, q)) + 5

from sklearn.cross_decomposition import PLSRegression

pls2 = PLSRegression(n_components=3)
pls2.fit(X, Y)
print("Wahre B (so dass: Y = XB + Err)")
print(B)
# Vergleiche pls2.coef_ mit B
print("Geschätzte B")
print(np.round(pls2.coef_, 1))
pls2.predict(X)
```
