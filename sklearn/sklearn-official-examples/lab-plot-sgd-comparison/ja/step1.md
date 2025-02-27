# データの読み込みと前処理

まず、scikit-learnから手書き数字のデータセットを読み込み、学習用とテスト用のセットに分割します。また、データを平均0、分散1にスケーリングします。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 数字のデータセットを読み込む
X, y = datasets.load_digits(return_X_y=True)

# データを学習用とテスト用に分割する
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# データを平均0、分散1にスケーリングする
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```
