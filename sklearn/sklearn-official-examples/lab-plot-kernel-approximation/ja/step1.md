# Pythonパッケージとデータセットのインポート、データセットの読み込み

```python
# 標準的な科学的Pythonのインポート
import matplotlib.pyplot as plt
import numpy as np
from time import time

# データセット、分類器、および性能指標をインポート
from sklearn import datasets, svm, pipeline
from sklearn.kernel_approximation import RBFSampler, Nystroem
from sklearn.decomposition import PCA

# 手書き数字データセット
digits = datasets.load_digits(n_class=9)
```
