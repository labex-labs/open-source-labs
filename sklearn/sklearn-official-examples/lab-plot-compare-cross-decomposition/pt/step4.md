# Regressão PLS com Resposta Univariada (PLS1)

Utilizamos o algoritmo de Regressão PLS com resposta univariada para estimar os valores de beta.

```python
n = 1000
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
y = X[:, 0] + 2 * X[:, 1] + np.random.normal(size=n * 1) + 5
pls1 = PLSRegression(n_components=3)
pls1.fit(X, y)
# observe que o número de componentes excede 1 (a dimensão de y)
print("Betas estimados")
print(np.round(pls1.coef_, 1))
```
