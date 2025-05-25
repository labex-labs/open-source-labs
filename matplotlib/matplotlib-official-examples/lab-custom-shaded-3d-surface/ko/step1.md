# 데이터 로드 및 형식 지정

이 단계에서는 3D 표면 플롯에 사용할 데이터를 로드하고 형식 지정합니다. "jacksboro_fault_dem.npz"라는 샘플 데이터 세트를 사용합니다.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cbook, cm
from matplotlib.colors import LightSource

# Load and format data
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']
nrows, ncols = z.shape
x = np.linspace(dem['xmin'], dem['xmax'], ncols)
y = np.linspace(dem['ymin'], dem['ymax'], nrows)
x, y = np.meshgrid(x, y)

region = np.s_[5:50, 5:50]
x, y, z = x[region], y[region], z[region]
```
