# 导入库

我们将首先导入本实验所需的库。我们将使用 scikit-learn 创建合成数据集，使用 MLPClassifier 构建 MLP 模型，使用 StandardScaler 对数据进行标准化，并使用 make_pipeline 创建一个由变换和分类器组成的管道。

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
```
