# 必要なライブラリをインポートする

まず、必要なライブラリをインポートします。データ操作と可視化に numpy と matplotlib を、回帰モデリングに scikit-learn からの HuberRegressor と Ridge を使用します。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import HuberRegressor, Ridge
```
