# 잡음이 있는 사인파 데이터 생성

잡음이 있는 사인파 데이터를 생성하는 것으로 시작합니다.

```python
import numpy as np

def func(x):
    return np.sin(2 * np.pi * x)

size = 25
rng = np.random.RandomState(1234)
x_train = rng.uniform(0.0, 1.0, size)
y_train = func(x_train) + rng.normal(scale=0.1, size=size)
x_test = np.linspace(0.0, 1.0, 100)
```
