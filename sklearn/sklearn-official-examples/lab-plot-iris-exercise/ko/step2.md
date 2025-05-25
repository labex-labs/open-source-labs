# 데이터 준비

다음으로, 훈련 및 테스트를 위한 데이터를 준비합니다. 데이터를 훈련용 90% 와 테스트용 10% 로 분할합니다.

```python
n_sample = len(X)

np.random.seed(0)
order = np.random.permutation(n_sample)
X = X[order]
y = y[order].astype(float)

X_train = X[: int(0.9 * n_sample)]
y_train = y[: int(0.9 * n_sample)]
X_test = X[int(0.9 * n_sample) :]
y_test = y[int(0.9 * n_sample) :]
```
