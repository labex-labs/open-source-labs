# 导入所需库

我们将首先导入所需的库，包括 scikit-learn、NumPy 和 Matplotlib。我们还将设置一个随机状态值以确保可重复性。

```python
import matplotlib.pyplot as plt
from collections import OrderedDict
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

RANDOM_STATE = 123
```
