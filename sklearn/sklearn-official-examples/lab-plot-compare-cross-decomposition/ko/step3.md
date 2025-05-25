# 다변량 반응 변수를 갖는 PLS 회귀 (PLS2)

다변량 반응 변수를 갖는 PLS 회귀 알고리즘을 사용하여 행렬 B 의 값을 추정합니다. 그런 다음 추정된 B 와 실제 B 를 비교합니다.

```python
n = 1000
q = 3
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
B = np.array([[1, 2] + [0] * (p - 2)] * q).T
# 각 Yj = 1*X1 + 2*X2 + 노이즈
Y = np.dot(X, B) + np.random.normal(size=n * q).reshape((n, q)) + 5

from sklearn.cross_decomposition import PLSRegression

pls2 = PLSRegression(n_components=3)
pls2.fit(X, Y)
print("실제 B (Y = XB + 오차)")
print(B)
# pls2.coef_와 B 를 비교
print("추정된 B")
print(np.round(pls2.coef_, 1))
pls2.predict(X)
```
