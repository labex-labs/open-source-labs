# 必要なライブラリをインポートして合成データを読み込む

必要なライブラリをインポートして合成データを読み込むことから始めます。合成乱数回帰データセットを生成し、すべてのエントリが非負になるようにすべてのターゲットを変換することでターゲットを変更し、単純な線形モデルではフィットさせることができない非線形ターゲットを取得するために指数関数を適用します。その後、線形回帰モデルを学習して予測に使用する前に、対数関数（np.log1p）と指数関数（np.expm1）を使ってターゲットを変換します。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.compose import TransformedTargetRegressor
from sklearn.linear_model import RidgeCV
from sklearn.metrics import median_absolute_error, r2_score, PredictionErrorDisplay

# Generate synthetic data
X, y = make_regression(n_samples=10_000, noise=100, random_state=0)

# Modify the targets
y = np.expm1((y + abs(y.min())) / 200)
y_trans = np.log1p(y)
```
