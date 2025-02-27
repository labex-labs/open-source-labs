# Regresión PLS con Respuesta Multivariada (PLS2)

Usamos el algoritmo de Regresión PLS con respuesta multivariada para estimar los valores de una matriz B. Luego comparamos la B estimada con la B real.

```python
n = 1000
q = 3
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
B = np.array([[1, 2] + [0] * (p - 2)] * q).T
# cada Yj = 1*X1 + 2*X2 + ruido
Y = np.dot(X, B) + np.random.normal(size=n * q).reshape((n, q)) + 5

from sklearn.cross_decomposition import PLSRegression

pls2 = PLSRegression(n_components=3)
pls2.fit(X, Y)
print("B real (tal que: Y = XB + Err)")
print(B)
# compare pls2.coef_ con B
print("B estimada")
print(np.round(pls2.coef_, 1))
pls2.predict(X)
```
