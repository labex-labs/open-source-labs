# 导入必要的库

首先，我们需要导入必要的库。我们将使用 scikit-learn 库进行机器学习和数据预处理。

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier, SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
```
