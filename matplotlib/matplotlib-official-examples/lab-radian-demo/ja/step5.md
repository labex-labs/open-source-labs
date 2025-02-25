# 2番目のサブプロットにデータをプロットする

matplotlib.pyplotのplot関数を使って、2番目のサブプロットにx値のコサインをプロットします。x軸を度で表すようにxunitsパラメータを使って指定します。

```python
from basic_units import degrees
axs[1].plot(x, cos(x), xunits=degrees)
```
