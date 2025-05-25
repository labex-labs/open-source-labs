# 데이터 생성

코사인 함수에서 30 개의 샘플을 생성하고, 샘플에 약간의 랜덤 노이즈를 추가합니다.

```python
def true_fun(X):
    return np.cos(1.5 * np.pi * X)

np.random.seed(0)

n_samples = 30

X = np.sort(np.random.rand(n_samples))
y = true_fun(X) + np.random.randn(n_samples) * 0.1
```
