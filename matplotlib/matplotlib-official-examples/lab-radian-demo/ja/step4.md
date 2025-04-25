# 最初のサブプロットにデータをプロットする

matplotlib.pyplot の plot 関数を使って、最初のサブプロットに x 値のコサインをプロットします。x 軸をラジアンで表すように xunits パラメータを使って指定します。

```python
from basic_units import cos
axs[0].plot(x, cos(x), xunits=radians)
```
