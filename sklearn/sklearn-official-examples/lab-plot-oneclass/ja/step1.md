# 必要なライブラリをインポートしてデータを生成する

最初のステップは、必要なライブラリをインポートしてデータを生成することです。データの生成と可視化には numpy と matplotlib を、1 クラス SVM モデルを構築するために scikit - learn を使用します。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# 学習用データを生成する
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]

# いくつかの通常の新奇な観測値を生成する
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]

# いくつかの異常な新奇な観測値を生成する
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```
