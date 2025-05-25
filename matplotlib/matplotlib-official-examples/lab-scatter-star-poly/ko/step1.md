# 라이브러리 가져오기 및 랜덤 시드 설정

필요한 라이브러리를 가져오고 결과의 재현성을 보장하기 위해 랜덤 시드를 설정하는 것으로 시작합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Set random seed
np.random.seed(19680801)
```
