# 라이브러리 가져오기 및 데이터 생성

먼저, 필요한 라이브러리를 가져오고 플롯할 데이터를 생성해야 합니다. 이 예제에서는 y 축에 대한 데이터를 생성하기 위해 정규 분포를 사용합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))
```
