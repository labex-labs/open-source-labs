# 必要なライブラリとデータをインポートする

まず、グリッドを作成するために必要なライブラリとデータをインポートする必要があります。グリッドを作成するために、描画には`matplotlib.pyplot`を、サンプルデータセットを取得するために`cbook`を、そしてグリッドを作成するために`ImageGrid`を使用します。

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid

# Get sample data
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
extent = (-3, 4, -4, 3)
```
