# 합성 데이터셋 생성

먼저, 샘플 수가 전체 특징 수보다 적은 데이터셋을 생성합니다. 이는 과소결정 시스템 (즉, 해결책이 유일하지 않고, 일반적인 최소 제곱법 자체를 적용할 수 없음) 을 초래합니다. 정규화는 목적 함수에 페널티 항을 도입하여 최적화 문제를 수정하고 시스템의 과소결정 특성을 완화하는 데 도움이 될 수 있습니다. 우리는 사인파 신호의 교대로 부호가 바뀌는 선형 결합인 대상 `y`를 생성할 것입니다. `X`의 100 개 주파수 중에서 가장 낮은 10 개만 `y` 생성에 사용되며, 나머지 특징은 정보가 없습니다. 이는 고차원 희소 특징 공간을 생성하며, 일정 정도의 L1 페널티가 필요합니다.

```python
import numpy as np

rng = np.random.RandomState(0)
n_samples, n_features, n_informative = 50, 100, 10
time_step = np.linspace(-2, 2, n_samples)
freqs = 2 * np.pi * np.sort(rng.rand(n_features)) / 0.01
X = np.zeros((n_samples, n_features))

for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step)

idx = np.arange(n_features)
true_coef = (-1) ** idx * np.exp(-idx / 10)
true_coef[n_informative:] = 0  # sparsify coef
y = np.dot(X, true_coef)

# introduce random phase using numpy.random.random_sample
# add some gaussian noise using numpy.random.normal
for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step + 2 * (rng.random_sample() - 0.5))
    X[:, i] += 0.2 * rng.normal(0, 1, n_samples)

y += 0.2 * rng.normal(0, 1, n_samples)

# split the data into train and test sets using train_test_split from sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=False)
```
