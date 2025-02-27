# KNNImputerを使った最近傍法による欠損値補完

`KNNImputer`クラスは、k-最近傍法を使って欠損値を埋めるための欠損値補完を提供します。欠損値を持つ各サンプルに対して最近傍点を見つけ、それらの近傍点の値に基づいて欠損した特徴量の値を補完します。

```python
from sklearn.impute import KNNImputer
nan = np.nan
X = [[1, 2, nan], [3, 4, 3], [nan, 6, 5], [8, 8, 7]]
imputer = KNNImputer(n_neighbors=2)
imputed_X = imputer.fit_transform(X)
```
