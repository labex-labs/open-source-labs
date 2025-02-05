# 导入库

在这一步中，我们导入必要的库：来自`sklearn.datasets`的`numpy`、`matplotlib`、`make_multilabel_classification`，来自`sklearn.multiclass`的`OneVsRestClassifier`和`SVC`，来自`sklearn.decomposition`的`PCA`和`CCA`。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA
```
