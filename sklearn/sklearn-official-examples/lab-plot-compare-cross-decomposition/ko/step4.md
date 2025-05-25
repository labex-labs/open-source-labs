# 단변량 반응 변수를 갖는 PLS 회귀 (PLS1)

단변량 반응 변수를 갖는 PLS 회귀 알고리즘을 사용하여 베타 값을 추정합니다.

```python
n = 1000
p = 10
X = np.random.normal(size=n * p).reshape((n, p))
y = X[:, 0] + 2 * X[:, 1] + np.random.normal(size=n * 1) + 5
pls1 = PLSRegression(n_components=3)
pls1.fit(X, y)
# y 의 차원 (1) 보다 성분의 수가 많음에 유의
print("추정된 베타 값")
print(np.round(pls1.coef_, 1))
```
