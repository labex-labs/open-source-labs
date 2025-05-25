# 라이브러리 가져오기 및 데이터 생성

먼저, 필요한 라이브러리를 가져오고 작업할 예제 데이터를 생성해야 합니다. 이 예제에서는 데이터를 생성하기 위해 numpy 를 사용하고, 시각화를 위해 matplotlib 을 사용합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# example data
x = np.arange(0.1, 4, 0.1)
y1 = np.exp(-1.0 * x)
y2 = np.exp(-0.5 * x)

# example variable error bar values
y1err = 0.1 + 0.1 * np.sqrt(x)
y2err = 0.1 + 0.1 * np.sqrt(x/2)
```
