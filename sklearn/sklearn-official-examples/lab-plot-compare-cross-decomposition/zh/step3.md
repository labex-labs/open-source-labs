# 具有多元响应的偏最小二乘回归（PLS2）

我们使用具有多元响应的偏最小二乘回归（PLS Regression）算法来估计矩阵B的值。然后，我们将估计出的B与真实的B进行比较。

```python
n = 1000
q = 3
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
B = np.array([[1, 2] + [0] * (p - 2)] * q).T
# 每个Yj = 1*X1 + 2*X2 + 噪声
Y = np.dot(X, B) + np.random.normal(size=n * q).reshape((n, q)) + 5

from sklearn.cross_decomposition import PLSRegression

pls2 = PLSRegression(n_components=3)
pls2.fit(X, Y)
print("真实的B（使得：Y = XB + 误差）")
print(B)
# 比较pls2.coef_与B
print("估计的B")
print(np.round(pls2.coef_, 1))
pls2.predict(X)
```
