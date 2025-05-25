# 필요한 라이브러리 가져오기

극좌표계에 산점도를 생성하려면 Matplotlib 및 NumPy 라이브러리를 가져와야 합니다. 또한 재현성을 위해 난수 시드 (random seed) 를 설정합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
```
