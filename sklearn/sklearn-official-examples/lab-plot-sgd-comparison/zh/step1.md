# 加载并预处理数据

我们将首先从scikit-learn中加载手写数字数据集，并将其拆分为训练集和测试集。我们还将对数据进行缩放，使其均值为零，方差为单位方差。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 加载数字数据集
X, y = datasets.load_digits(return_X_y=True)

# 将数据拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 对数据进行缩放，使其均值为零，方差为单位方差
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```
