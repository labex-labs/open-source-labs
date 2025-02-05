# 加载数据集

首先，我们需要从scikit-learn中加载数字数据集，并将其拆分为特征和标签。

```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_digits(return_X_y=True)
```
