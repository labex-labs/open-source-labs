# Python 包和数据集导入、加载数据集

```python
# 标准的科学 Python 导入
import matplotlib.pyplot as plt
import numpy as np
from time import time

# 导入数据集、分类器和性能指标
from sklearn import datasets, svm, pipeline
from sklearn.kernel_approximation import RBFSampler, Nystroem
from sklearn.decomposition import PCA

# 数字数据集
digits = datasets.load_digits(n_class=9)
```
