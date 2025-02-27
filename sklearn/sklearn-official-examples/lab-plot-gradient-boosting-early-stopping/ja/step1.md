# 必要なライブラリとデータの読み込み

まず、必要なライブラリとデータを読み込む必要があります。勾配ブースティングの実装にはscikit - learnライブラリを使用します。

```python
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import ensemble
from sklearn import datasets
from sklearn.model_selection import train_test_split

data_list = [
    datasets.load_iris(return_X_y=True),
    datasets.make_classification(n_samples=800, random_state=0),
    datasets.make_hastie_10_2(n_samples=2000, random_state=0),
]
names = ["Iris Data", "Classification Data", "Hastie Data"]
n_estimators = 200
```
