# データセットの読み込み

scikit - learn の`load_digits()`関数を使って数字のデータセットを読み込みます。この関数はデータセットの特徴とラベルを返します。

```python
import numpy as np
from sklearn.datasets import load_digits

data, labels = load_digits(return_X_y=True)
(n_samples, n_features), n_digits = data.shape, np.unique(labels).size
```
