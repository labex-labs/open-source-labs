# 라이브러리 임포트 및 랜덤 시드 설정

재현성을 위해 필요한 라이브러리를 임포트하고 랜덤 시드를 설정하는 것으로 시작합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.rcParams['font.size'] = 8.0

# Fixing random state for reproducibility
np.random.seed(19680801)
```
