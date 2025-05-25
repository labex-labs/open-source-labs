# 데이터 생성

먼저, 모델에 적합시킬 수 있는 샘플 데이터를 생성해야 합니다. NumPy 를 사용하여 100 개의 샘플을 생성하며, 각 샘플은 30 개의 특징과 40 개의 작업을 가집니다. 또한 5 개의 관련 특징을 무작위로 선택하고, 랜덤한 주파수와 위상을 가진 사인파를 사용하여 이들에 대한 계수를 생성합니다. 마지막으로 데이터에 랜덤 노이즈를 추가합니다.

```python
import numpy as np

rng = np.random.RandomState(42)

# 랜덤 주파수와 위상을 가진 사인파를 사용하여 2 차원 계수를 생성
n_samples, n_features, n_tasks = 100, 30, 40
n_relevant_features = 5
coef = np.zeros((n_tasks, n_features))
times = np.linspace(0, 2 * np.pi, n_tasks)
for k in range(n_relevant_features):
    coef[:, k] = np.sin((1.0 + rng.randn(1)) * times + 3 * rng.randn(1))

X = rng.randn(n_samples, n_features)
Y = np.dot(X, coef.T) + rng.randn(n_samples, n_tasks)
```
