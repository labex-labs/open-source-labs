# 데이터셋 생성

단일 특징 `x`와 선형 관계를 사용하여 동일한 기대값을 갖는 두 개의 합성 데이터셋을 생성할 것입니다. 이 데이터셋에 이종분산 정규 노이즈와 비대칭 파레토 노이즈를 추가할 것입니다.

```python
import numpy as np

rng = np.random.RandomState(42)
x = np.linspace(start=0, stop=10, num=100)
X = x[:, np.newaxis]
y_true_mean = 10 + 0.5 * x

# 이종분산 정규 노이즈
y_normal = y_true_mean + rng.normal(loc=0, scale=0.5 + 0.5 * x, size=x.shape[0])

# 비대칭 파레토 노이즈
a = 5
y_pareto = y_true_mean + 10 * (rng.pareto(a, size=x.shape[0]) - 1 / (a - 1))
```
