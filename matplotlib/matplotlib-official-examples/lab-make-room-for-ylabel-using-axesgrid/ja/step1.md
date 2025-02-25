# ライブラリのインポートとグラフの作成

最初のステップは、必要なライブラリをインポートしてグラフを作成することです。私たちは、`matplotlib.pyplot`モジュールを使ってグラフを作成し、`mpl_toolkits.axes_grid1`モジュールを使ってy軸のラベルにスペースを作ります。

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
```
