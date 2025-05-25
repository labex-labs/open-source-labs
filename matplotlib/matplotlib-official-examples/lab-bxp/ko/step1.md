# 라이브러리 가져오기 및 데이터 생성

필요한 라이브러리를 가져오고 가짜 데이터를 생성하는 것으로 시작합니다.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Generate fake data
np.random.seed(19680801)
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
```
