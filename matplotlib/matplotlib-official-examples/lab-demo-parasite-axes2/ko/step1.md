# 라이브러리 임포트

먼저 필요한 라이브러리를 임포트해야 합니다. 플로팅을 위해 `matplotlib.pyplot`을 사용하고, 기생 축 (parasite axis) 을 생성하기 위해 `mpl_toolkits`을 사용합니다.

```python
import matplotlib.pyplot as plt
from mpl_toolkits import axisartist
from mpl_toolkits.axes_grid1 import host_subplot
```
