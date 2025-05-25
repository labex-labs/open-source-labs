# 필요한 라이브러리 가져오기

Matplotlib 과 NumPy 와 같은 필요한 라이브러리를 먼저 가져오는 것으로 시작합니다. 또한 결과의 재현성을 보장하기 위해 NumPy 에 대한 랜덤 시드 (random seed) 를 설정합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
```
