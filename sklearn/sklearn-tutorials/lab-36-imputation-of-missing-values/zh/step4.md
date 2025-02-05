# 使用KNNImputer进行最近邻插补

`KNNImputer`类提供了使用k近邻方法填充缺失值的插补功能。它为每个有缺失值的样本找到最近邻，并根据邻居的值插补缺失的特征值。

```python
from sklearn.impute import KNNImputer
nan = np.nan
X = [[1, 2, nan], [3, 4, 3], [nan, 6, 5], [8, 8, 7]]
imputer = KNNImputer(n_neighbors=2)
imputed_X = imputer.fit_transform(X)
```
