# データセットの準備

まず、S曲線データセットを生成します。

```python
import matplotlib.pyplot as plt
from matplotlib import ticker

# matplotlib < 3.2で3D投影を行うために必要なインポートですが、使用しません
import mpl_toolkits.mplot3d  # noqa: F401

from sklearn import manifold, datasets

n_samples = 1500
S_points, S_color = datasets.make_s_curve(n_samples, random_state=0)

```
