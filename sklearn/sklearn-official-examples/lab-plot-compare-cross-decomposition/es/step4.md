# Regresión PLS con Respuesta Univariada (PLS1)

Usamos el algoritmo de Regresión PLS con respuesta univariada para estimar los valores de beta.

```python
n = 1000
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
y = X[:, 0] + 2 * X[:, 1] + np.random.normal(size=n * 1) + 5
pls1 = PLSRegression(n_components=3)
pls1.fit(X, y)
# observe que el número de componentes excede 1 (la dimensión de y)
print("Betas estimadas")
print(np.round(pls1.coef_, 1))
```
