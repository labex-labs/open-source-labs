# ライブラリのインポート

この実験に必要なライブラリをインポートして始めましょう。scikit-learn ライブラリを使ってデータセットを取得し、モデルを学習させ、モデルの性能を評価します。

```python
import time
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state
```
