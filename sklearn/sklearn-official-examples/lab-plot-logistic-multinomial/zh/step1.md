# 导入库

我们将首先导入本实验所需的库。我们将使用 scikit-learn 库来生成数据集并训练逻辑回归模型，使用 matplotlib 库来绘制决策边界。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
```
