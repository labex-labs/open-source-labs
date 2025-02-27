# 必要なライブラリをインポートしてデータを生成する

まず、必要なライブラリをインポートして、分類に適したデータセットを生成する必要があります。この例では、Scikit-learnの`make_blobs`関数を使って50個の分離可能なポイントを生成します。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_blobs

# we create 50 separable points
X, Y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)
```
