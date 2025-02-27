# Регрессия PLS с одномерным откликом (PLS1)

Мы используем алгоритм Регрессии PLS с одномерным откликом для оценки значений beta.

```python
n = 1000
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
y = X[:, 0] + 2 * X[:, 1] + np.random.normal(size=n * 1) + 5
pls1 = PLSRegression(n_components=3)
pls1.fit(X, y)
# обратите внимание, что количество компонентов превышает 1 (размерность y)
print("Оцененные betas")
print(np.round(pls1.coef_, 1))
```
