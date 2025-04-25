# データセットの読み込みと準備

まず、糖尿病データセットを読み込み、準備します。この演習では最初の 150 サンプルのみを使用します。

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
X = X[:150]
y = y[:150]
```
