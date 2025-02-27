# データの読み込み

Iris データセットを読み込み、可視化の目的で最初の 2 つの特徴のみを選択して始めます。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y!= 0, :2]
y = y[y!= 0]
```
