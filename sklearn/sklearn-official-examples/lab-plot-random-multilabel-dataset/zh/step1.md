# 导入所需库并定义常量

首先，我们需要导入所需的库，并定义用于生成多标签数据集的颜色和随机种子常量。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification as make_ml_clf

COLORS = np.array(
    [
        "!",
        "#FF3333",  # 红色
        "#0198E1",  # 蓝色
        "#BF5FFF",  # 紫色
        "#FCD116",  # 黄色
        "#FF7216",  # 橙色
        "#4DBD33",  # 绿色
        "#87421F",  # 棕色
    ]
)

# 多次调用 make_multilabel_classification 时使用相同的随机种子，以确保相同的分布
RANDOM_SEED = np.random.randint(2**10)
```
