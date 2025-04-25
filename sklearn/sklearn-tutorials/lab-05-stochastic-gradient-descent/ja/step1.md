# 必要なライブラリをインポートする

まず、必要なライブラリをインポートする必要があります。機械学習とデータ前処理には scikit-learn ライブラリを使用します。

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier, SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
```
