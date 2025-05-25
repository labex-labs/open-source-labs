# 데이터셋에 강력한 이상치 추가

데이터셋에 네 개의 강력한 이상치를 추가합니다. 정규 분포를 사용하여 이러한 이상치에 대한 랜덤 값을 생성합니다. 그런 다음 이러한 이상치를 데이터셋에 추가합니다.

```python
X_outliers = rng.normal(0, 0.5, size=(4, 1))
y_outliers = rng.normal(0, 2.0, size=4)
X_outliers[:2, :] += X.max() + X.mean() / 4.0
X_outliers[2:, :] += X.min() - X.mean() / 4.0
y_outliers[:2] += y.min() - y.mean() / 4.0
y_outliers[2:] += y.max() + y.mean() / 4.0
X = np.vstack((X, X_outliers))
y = np.concatenate((y, y_outliers))
```
