# 糖尿病データセットを読み込む

まず、scikit - learnから糖尿病データセットを読み込み、データセットから1つの特徴のみを選択します。

```python
import numpy as np
from sklearn import datasets

# 糖尿病データセットを読み込む
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# 1つの特徴のみを使用する
diabetes_X = diabetes_X[:, np.newaxis, 2]
```
