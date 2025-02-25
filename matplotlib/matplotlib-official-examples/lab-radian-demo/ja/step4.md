# 最初のサブプロットにデータをプロットする

matplotlib.pyplotのplot関数を使って、最初のサブプロットにx値のコサインをプロットします。x軸をラジアンで表すようにxunitsパラメータを使って指定します。

```python
from basic_units import cos
axs[0].plot(x, cos(x), xunits=radians)
```
