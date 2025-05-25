# 라이브러리 가져오기 및 데이터 설정

먼저, 필요한 라이브러리를 가져오고 플롯할 데이터를 설정해야 합니다. 이 예제에서는 세 개의 사인파를 플롯하고, 여기에 약간의 무작위 노이즈를 추가할 것입니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Set up data
np.random.seed(19680801)

X = np.linspace(0.5, 3.5, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
Y3 = np.random.uniform(Y1, Y2, len(X))
```
