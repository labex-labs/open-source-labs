# 데이터셋 생성

합성 데이터셋을 생성합니다. 실제 생성 과정은 1 차원 벡터를 입력받아 그 사인 값을 계산합니다.

```python
import numpy as np

rng = np.random.RandomState(0)
data = np.linspace(0, 30, num=1_000).reshape(-1, 1)
target = np.sin(data).ravel()

training_sample_indices = rng.choice(np.arange(0, 400), size=40, replace=False)
training_data = data[training_sample_indices]
training_noisy_target = target[training_sample_indices] + 0.5 * rng.randn(
    len(training_sample_indices)
)
```
