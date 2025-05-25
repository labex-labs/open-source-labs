# 데이터셋 준비

S-곡선 데이터셋을 생성합니다.

```python
import matplotlib.pyplot as plt
from matplotlib import ticker

# matplotlib < 3.2 에서 3D 투영을 위해 필요하지만 사용되지 않는 import
import mpl_toolkits.mplot3d  # noqa: F401

from sklearn import manifold, datasets

n_samples = 1500
S_points, S_color = datasets.make_s_curve(n_samples, random_state=0)
```
