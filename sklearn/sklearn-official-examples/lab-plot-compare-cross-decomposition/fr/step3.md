# Régression PLS avec réponse multivariée (PLS2)

Nous utilisons l'algorithme de régression PLS avec réponse multivariée pour estimer les valeurs d'une matrice B. Nous comparons ensuite l'estimation de B avec la vraie B.

```python
n = 1000
q = 3
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
B = np.array([[1, 2] + [0] * (p - 2)] * q).T
# chaque Yj = 1*X1 + 2*X2 + bruit
Y = np.dot(X, B) + np.random.normal(size=n * q).reshape((n, q)) + 5

from sklearn.cross_decomposition import PLSRegression

pls2 = PLSRegression(n_components=3)
pls2.fit(X, Y)
print("Vraie B (telle que : Y = XB + Err)")
print(B)
# comparer pls2.coef_ avec B
print("Estimation de B")
print(np.round(pls2.coef_, 1))
pls2.predict(X)
```
