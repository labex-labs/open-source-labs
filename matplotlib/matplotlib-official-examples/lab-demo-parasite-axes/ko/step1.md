# 필요한 라이브러리 가져오기

먼저, 필요한 라이브러리를 가져와야 합니다. 이 랩에서는 플로팅을 위해 `matplotlib.pyplot`을 사용하고, 기생 축 (parasite axes) 을 생성하기 위해 `mpl_toolkits.axes_grid1.parasite_axes.HostAxes` 및 `mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes`를 사용합니다.

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.parasite_axes import HostAxes
```
