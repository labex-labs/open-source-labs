# 必要なライブラリをインポートしてデータを読み込む

必要なライブラリをインポートしてデータセットを読み込みましょう。この例では、Irisデータセットを使用します。

```python
import numpy as np
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_iris
from sklearn.linear_model import Ridge

np.random.seed(0)
X, y = load_iris(return_X_y=True)
```
