# 必要なライブラリをインポートする

まず、必要なライブラリをインポートします。データ操作と可視化にnumpyとmatplotlibを、回帰モデリングにscikit-learnからのHuberRegressorとRidgeを使用します。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import HuberRegressor, Ridge
```
