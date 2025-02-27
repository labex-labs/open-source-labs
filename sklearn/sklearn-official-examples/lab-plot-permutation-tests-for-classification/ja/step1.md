# データセットを読み込み、ランダムな特徴量を生成する

我々は、3種類のアヤメから測定されたデータからなるアヤメデータセットを使用し、アヤメデータセットのクラスラベルと相関のないいくつかのランダムな特徴量データ（すなわち、20個の特徴量）を生成します。

```python
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

n_uncorrelated_features = 20
rng = np.random.RandomState(seed=0)
X_rand = rng.normal(size=(X.shape[0], n_uncorrelated_features))
```
