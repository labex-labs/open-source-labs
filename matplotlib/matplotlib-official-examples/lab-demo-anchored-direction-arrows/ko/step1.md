# 필요한 라이브러리 가져오기

먼저 Matplotlib, NumPy, Matplotlib 폰트 관리자, 그리고 mpl_toolkits.axes_grid1 에서 AnchoredDirectionArrows 와 같은 필요한 라이브러리를 가져와야 합니다. 이러한 라이브러리를 사용하여 앵커된 방향 화살표를 만들 것입니다.

```python
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.font_manager as fm
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredDirectionArrows
```
