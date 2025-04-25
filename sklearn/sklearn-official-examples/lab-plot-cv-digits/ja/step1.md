# データセットの読み込み

まず、scikit-learn から数字データセットを読み込み、特徴量とラベルに分割する必要があります。

```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_digits(return_X_y=True)
```
