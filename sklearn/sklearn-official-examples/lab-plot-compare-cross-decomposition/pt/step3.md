# Regressão PLS com Resposta Multivariada (PLS2)

Utilizamos o algoritmo de Regressão PLS com resposta multivariada para estimar os valores de uma matriz B. Em seguida, comparamos a B estimada com a B verdadeira.

```python
n = 1000
q = 3
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
B = np.array([[1, 2] + [0] * (p - 2)] * q).T
# cada Yj = 1*X1 + 2*X2 + ruído
Y = np.dot(X, B) + np.random.normal(size=n * q).reshape((n, q)) + 5

from sklearn.cross_decomposition import PLSRegression

pls2 = PLSRegression(n_components=3)
pls2.fit(X, Y)
print("B Verdadeiro (tal que: Y = XB + Erro)")
print(B)
# comparar pls2.coef_ com B
print("B Estimado")
print(np.round(pls2.coef_, 1))
pls2.predict(X)
```
