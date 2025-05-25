# Triangulation 객체 생성

먼저, Triangulation 객체를 생성해야 합니다. `matplotlib.tri`에서 `Triangulation` 클래스를 사용합니다. 이 예제에서는 임의의 데이터를 사용하여 Triangulation 객체를 생성합니다.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import Triangulation

# Generate random data
x = np.random.rand(10)
y = np.random.rand(10)
triang = Triangulation(x, y)
```
