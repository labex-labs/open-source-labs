# 2 番目のサブプロットにデータをプロットする

matplotlib.pyplot の plot 関数を使って、2 番目のサブプロットに x 値のコサインをプロットします。x 軸を度で表すように xunits パラメータを使って指定します。

```python
from basic_units import degrees
axs[1].plot(x, cos(x), xunits=degrees)
```
