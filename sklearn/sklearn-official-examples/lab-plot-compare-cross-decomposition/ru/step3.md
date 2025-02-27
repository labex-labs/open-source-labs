# Регрессия PLS с многомерным откликом (PLS2)

Мы используем алгоритм Регрессии PLS с многомерным откликом для оценки значений матрицы B. Затем мы сравниваем оцененную B с истинной B.

```python
n = 1000
q = 3
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
B = np.array([[1, 2] + [0] * (p - 2)] * q).T
# для каждого Yj = 1*X1 + 2*X2 + шум
Y = np.dot(X, B) + np.random.normal(size=n * q).reshape((n, q)) + 5

from sklearn.cross_decomposition import PLSRegression

pls2 = PLSRegression(n_components=3)
pls2.fit(X, Y)
print("Истинная B (такая что: Y = XB + Err)")
print(B)
# сравним pls2.coef_ с B
print("Оцененная B")
print(np.round(pls2.coef_, 1))
pls2.predict(X)
```
