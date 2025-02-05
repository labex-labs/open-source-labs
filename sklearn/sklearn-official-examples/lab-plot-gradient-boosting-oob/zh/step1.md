# 生成数据

第一步是生成一些示例数据，用于训练和测试我们的模型。我们将使用 `sklearn.datasets` 模块中的 `make_classification` 函数来生成一个具有 3 个信息特征的随机二分类问题。

```python
import numpy as np
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=3, n_informative=3,
                           n_redundant=0, n_classes=2, random_state=1)
```
