# 具有单变量响应的偏最小二乘回归（PLS1）

我们使用具有单变量响应的偏最小二乘回归（PLS Regression）算法来估计β的值。

```python
n = 1000
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
y = X[:, 0] + 2 * X[:, 1] + np.random.normal(size=n * 1) + 5
pls1 = PLSRegression(n_components=3)
pls1.fit(X, y)
# 注意，成分数量超过了 1（y 的维度）
print("估计的β值")
print(np.round(pls1.coef_, 1))
```
