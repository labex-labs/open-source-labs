# データセットの読み込み

このステップでは、scikit-learnライブラリから糖尿病データセットを読み込み、データを標準化します。

```python
from sklearn import datasets

# 糖尿病データセットを読み込む
X, y = datasets.load_diabetes(return_X_y=True)

# データを標準化する
X /= X.std(axis=0)
```
