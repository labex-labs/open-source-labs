# 必要なライブラリをインポートする

まず、必要なライブラリをインポートする必要があります。この実験では、グラフ描画に`matplotlib.pyplot`を、寄生虫軸を作成するために`mpl_toolkits.axes_grid1.parasite_axes.HostAxes`と`mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes`を使用します。

```python
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.parasite_axes import HostAxes
```
