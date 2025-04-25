# 导入所需库

我们将首先导入所需的库，包括用于数据处理和可视化的 numpy 和 matplotlib，以及用于回归建模的来自 scikit-learn 的 HuberRegressor 和 Ridge。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import HuberRegressor, Ridge
```
