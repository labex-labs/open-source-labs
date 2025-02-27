# 単変量応答付きPLS回帰(PLS1)

betaの値を推定するために、単変量応答付きPLS回帰アルゴリズムを使用します。

```python
n = 1000
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
y = X[:, 0] + 2 * X[:, 1] + np.random.normal(size=n * 1) + 5
pls1 = PLSRegression(n_components=3)
pls1.fit(X, y)
# コンポーネントの数が1(yの次元)を超えていることに注意
print("Estimated betas")
print(np.round(pls1.coef_, 1))
```
