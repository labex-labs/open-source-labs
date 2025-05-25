# 필요한 라이브러리 가져오기 및 데이터 생성

```python
import matplotlib.pyplot as plt
import numpy as np

# Create data
t = np.arange(0.0, 100.0, 0.1)
s = np.sin(0.1 * np.pi * t) * np.exp(-t * 0.01)
```

먼저, 필요한 라이브러리, 즉 Matplotlib 와 NumPy 를 가져옵니다. 그런 다음 플롯할 데이터를 생성합니다. 이 예제에서는 numpy 배열 "t"를 생성하고 t 를 사용하여 다른 numpy 배열 "s"를 계산합니다.
