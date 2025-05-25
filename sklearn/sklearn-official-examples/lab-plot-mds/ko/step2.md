# 데이터 생성

다음으로 numpy 를 사용하여 잡음 데이터 세트를 생성합니다. 각각 2 개의 특징을 가진 20 개의 샘플을 생성할 것입니다.

```python
EPSILON = np.finfo(np.float32).eps
n_samples = 20
seed = np.random.RandomState(seed=3)
X_true = seed.randint(0, 20, 2 * n_samples).astype(float)
X_true = X_true.reshape((n_samples, 2))
# 데이터를 중심화합니다.
X_true -= X_true.mean()
```
