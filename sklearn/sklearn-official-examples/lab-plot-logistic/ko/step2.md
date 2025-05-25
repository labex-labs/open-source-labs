# 가상 데이터셋 생성

다음 단계는 가우시안 노이즈가 포함된 직선 형태의 가상 데이터셋을 생성하는 것입니다. `numpy`를 사용하여 이 데이터셋을 생성합니다.

```python
# 가상 데이터셋 생성, 가우시안 노이즈가 포함된 직선입니다.
xmin, xmax = -5, 5
n_samples = 100
np.random.seed(0)
X = np.random.normal(size=n_samples)
y = (X > 0).astype(float)
X[X > 0] *= 4
X += 0.3 * np.random.normal(size=n_samples)

X = X[:, np.newaxis]
```
