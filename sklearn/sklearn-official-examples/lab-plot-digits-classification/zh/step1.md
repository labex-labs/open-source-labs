# 导入库

首先，我们需要导入必要的库。我们将使用`matplotlib`进行可视化，从`sklearn`中导入`datasets`和`metrics`来加载和评估数据集，并使用`svm`来训练支持向量机。

```python
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
```
