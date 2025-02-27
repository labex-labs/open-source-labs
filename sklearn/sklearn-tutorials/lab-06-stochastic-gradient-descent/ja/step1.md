# ライブラリのインポート

まず、この実験（Lab）で必要なライブラリをインポートする必要があります。その中には scikit-learn も含まれます。

```python
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```
