# 导入库

我们将首先为本实验导入必要的库。我们将使用 scikit-learn 库来获取数据集、训练模型并评估模型的性能。

```python
import time
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state
```
