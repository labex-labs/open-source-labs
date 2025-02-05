# 导入必要的库

首先，我们需要导入必要的库，包括MLPClassifier、MinMaxScaler、datasets和matplotlib.pyplot。我们还将导入ConvergenceWarning以在训练期间忽略收敛警告。

```python
import warnings

import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn import datasets
from sklearn.exceptions import ConvergenceWarning
```
