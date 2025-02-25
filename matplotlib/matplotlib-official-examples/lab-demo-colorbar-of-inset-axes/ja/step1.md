# ライブラリとデータのインポート

まず、グラフで使用する必要なライブラリとデータをインポートします。

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes

fig, ax = plt.subplots(figsize=[5, 4])

Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
extent = (-3, 4, -4, 3)
```
