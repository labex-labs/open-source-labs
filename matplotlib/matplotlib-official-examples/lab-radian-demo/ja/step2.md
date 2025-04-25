# データを作成する

0 から 15 まで 0.01 刻みで値の配列を作成し、basic_units パッケージの radians 関数を使ってそれらをラジアンに変換します。

```python
from basic_units import radians
x = [val*radians for val in np.arange(0, 15, 0.01)]
```
