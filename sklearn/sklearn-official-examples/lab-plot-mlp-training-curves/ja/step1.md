# 必要なライブラリをインポートする

まず、MLPClassifier、MinMaxScaler、datasets、および matplotlib.pyplot を含む必要なライブラリをインポートする必要があります。また、訓練中の収束警告を無視するために ConvergenceWarning もインポートします。

```python
import warnings

import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn import datasets
from sklearn.exceptions import ConvergenceWarning
```
