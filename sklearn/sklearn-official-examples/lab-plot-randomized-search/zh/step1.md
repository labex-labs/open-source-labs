# 导入必要的库并加载数据

我们将首先导入必要的库，并从scikit-learn中加载数字数据集。

```python
import numpy as np
from time import time
import scipy.stats as stats
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.datasets import load_digits
from sklearn.linear_model import SGDClassifier

# load digits dataset
X, y = load_digits(return_X_y=True, n_class=3)
```
