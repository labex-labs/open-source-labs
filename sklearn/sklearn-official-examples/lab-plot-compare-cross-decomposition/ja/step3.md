# 多変量応答付き PLS 回帰 (PLS2)

行列 B の値を推定するために、多変量応答付き PLS 回帰アルゴリズムを使用します。その後、推定された B と真の B を比較します。

```python
n = 1000
q = 3
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
B = np.array([[1, 2] + [0] * (p - 2)] * q).T
# 各 Yj = 1*X1 + 2*X2 + ノイズ
Y = np.dot(X, B) + np.random.normal(size=n * q).reshape((n, q)) + 5

from sklearn.cross_decomposition import PLSRegression

pls2 = PLSRegression(n_components=3)
pls2.fit(X, Y)
print("True B (such that: Y = XB + Err)")
print(B)
# pls2.coef_ と B を比較
print("Estimated B")
print(np.round(pls2.coef_, 1))
pls2.predict(X)
```
