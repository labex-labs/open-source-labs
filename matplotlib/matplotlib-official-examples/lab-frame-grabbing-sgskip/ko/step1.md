# 필요한 라이브러리 임포트

먼저 애니메이션을 생성하는 데 필요한 라이브러리를 임포트해야 합니다. 난수를 생성하기 위해 `numpy`를, 플로팅을 위해 `matplotlib`를, 프레임을 파일에 쓰기 위해 `FFMpegWriter`를 사용합니다.

```python
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
```
