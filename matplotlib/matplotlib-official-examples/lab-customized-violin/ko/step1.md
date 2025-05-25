# 테스트 데이터 생성

먼저, 바이올린 플롯에 사용할 테스트 데이터를 생성합니다. NumPy 를 사용하여 표준 편차가 증가하는 100 개의 정규 분포 값을 가진 네 개의 배열을 생성합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# create test data
np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
```
