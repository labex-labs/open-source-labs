# 데이터셋 생성

다음으로 잡음이 포함된 사인 곡선을 따르는 데이터셋을 생성합니다.

```python
# 매개변수
n_samples = 100

# 사인 곡선을 따르는 랜덤 샘플 생성
np.random.seed(0)
X = np.zeros((n_samples, 2))
step = 4.0 * np.pi / n_samples

for i in range(X.shape[0]):
    x = i * step - 6.0
    X[i, 0] = x + np.random.normal(0, 0.1)
    X[i, 1] = 3.0 * (np.sin(x) + np.random.normal(0, 0.2))
```
