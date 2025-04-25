# 必要なライブラリをインポートしてデータを読み込む

必要なライブラリをインポートし、scikit-learn からの手書き数字データセットを読み込むことから始めます。

```python
import numpy as np
from time import time
import scipy.stats as stats
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.datasets import load_digits
from sklearn.linear_model import SGDClassifier

# load digits dataset
X, y = load_digits(return_X_y=True, n_class=3)
```
