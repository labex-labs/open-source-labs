# 棒グラフ用のデータを作成する

このステップでは、棒グラフ用のデータを作成する必要があります。棒グラフに使用する値の配列を作成するために、numpy ライブラリを使用します。

```python
from basic_units import cm, inch

cms = cm * np.arange(0, 10, 2)
bottom = 0 * cm
width = 0.8 * cm
```
