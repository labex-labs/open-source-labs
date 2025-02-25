# データを作成する

0から15まで0.01刻みで値の配列を作成し、basic_unitsパッケージのradians関数を使ってそれらをラジアンに変換します。

```python
from basic_units import radians
x = [val*radians for val in np.arange(0, 15, 0.01)]
```
