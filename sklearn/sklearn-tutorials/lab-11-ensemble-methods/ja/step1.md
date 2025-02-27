# 必要なライブラリをインポートする

まずは、必要な依存関係（ライブラリ）をインポートしましょう。

```python
import numpy as np
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
```
