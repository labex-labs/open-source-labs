# データを生成する

最初のステップは、モデルの学習とテストに使用できるサンプルデータを生成することです。`sklearn.datasets` モジュールの `make_classification` 関数を使用して、3 つの情報的な特徴を持つランダムな 2 値分類問題を生成します。

```python
import numpy as np
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=3, n_informative=3,
                           n_redundant=0, n_classes=2, random_state=1)
```
