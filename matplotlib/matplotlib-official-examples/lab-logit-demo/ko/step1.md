# 필요한 라이브러리 가져오기 및 데이터 설정

`math`, `numpy`, 그리고 `matplotlib.pyplot` 라이브러리를 가져오고 플롯에 사용할 데이터를 설정합니다.

```python
import math
import numpy as np
import matplotlib.pyplot as plt

xmax = 10
x = np.linspace(-xmax, xmax, 10000)
cdf_norm = [math.erf(w / np.sqrt(2)) / 2 + 1 / 2 for w in x]
cdf_laplacian = np.where(x < 0, 1 / 2 * np.exp(x), 1 - 1 / 2 * np.exp(-x))
cdf_cauchy = np.arctan(x) / np.pi + 1 / 2
```
