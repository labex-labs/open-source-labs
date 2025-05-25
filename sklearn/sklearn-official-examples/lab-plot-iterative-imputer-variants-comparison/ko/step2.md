# 데이터셋 로드

Scikit-Learn 에서 캘리포니아 주택 데이터셋을 로드합니다. 계산 시간을 줄이기 위해 2,000 개의 샘플만 사용합니다.

```python
N_SPLITS = 5

rng = np.random.RandomState(0)

X_full, y_full = fetch_california_housing(return_X_y=True)
X_full = X_full[::10]
y_full = y_full[::10]
n_samples, n_features = X_full.shape
```
