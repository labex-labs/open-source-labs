# ライブラリのインポート

このステップでは、必要なライブラリをインポートします。`numpy`、`matplotlib`、`sklearn.datasets` からの `make_multilabel_classification`、`sklearn.multiclass` からの `OneVsRestClassifier` と `SVC`、`sklearn.decomposition` からの `PCA` と `CCA` です。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA
```
