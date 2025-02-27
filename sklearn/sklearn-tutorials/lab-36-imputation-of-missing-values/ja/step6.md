# MissingIndicatorを使った欠損値補完された値のマーキング

`MissingIndicator`変換器は、データセットにおける欠損値の存在を示すのに役立ちます。欠損値補完と併用して、どの値が欠損値補完されたかに関する情報を保持するために使用できます。この変換器は、データセットにおける欠損値の存在を示す2値行列を返します。

```python
from sklearn.impute import MissingIndicator
X = np.array([[-1, -1, 1, 3], [4, -1, 0, -1], [8, -1, 1, 0]])
indicator = MissingIndicator()
mask_missing_values_only = indicator.fit_transform(X)
```
