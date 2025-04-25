# ランダムデータの生成

アルゴリズムをテストするために、いくつかのランダムデータを生成します。50 個の特徴量を持つ 200 個のサンプルを作成し、各特徴量に対して真の係数を 3 とします。その後、係数を閾値処理して非負にします。最後に、サンプルにいくらかのノイズを追加します。

```python
import numpy as np

np.random.seed(42)

n_samples, n_features = 200, 50
X = np.random.randn(n_samples, n_features)
true_coef = 3 * np.random.randn(n_features)
true_coef[true_coef < 0] = 0
y = np.dot(X, true_coef)
y += 5 * np.random.normal(size=(n_samples,))
```
