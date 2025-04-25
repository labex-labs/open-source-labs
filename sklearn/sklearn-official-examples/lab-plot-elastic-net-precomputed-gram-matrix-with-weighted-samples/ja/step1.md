# データセットの読み込みとサンプル重みの作成

まず、データセットを読み込み、いくつかのサンプル重みを作成します。scikit-learn の`make_regression`関数を使って、100,000 個のサンプルを持つランダムな回帰データセットを生成します。その後、対数正規分布の重みベクトルを生成し、サンプルの総数に合計するように正規化します。

```python
import numpy as np
from sklearn.datasets import make_regression

rng = np.random.RandomState(0)

n_samples = int(1e5)
X, y = make_regression(n_samples=n_samples, noise=0.5, random_state=rng)

sample_weight = rng.lognormal(size=n_samples)
# normalize the sample weights
normalized_weights = sample_weight * (n_samples / (sample_weight.sum()))
```
