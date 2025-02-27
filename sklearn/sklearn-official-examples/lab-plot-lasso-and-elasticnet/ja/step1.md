# 合成データセットの生成

まず、サンプル数が特徴量の総数より少ないデータセットを生成します。これにより、解が一意でない、つまり未定義系が生じ、通常の最小二乗法を単独で適用することができません。正則化は目的関数にペナルティ項を導入し、最適化問題を修正し、系の未定義な性質を軽減するのに役立ちます。正弦波信号の符号が交互になる線形結合であるターゲット `y` を生成します。`X` の 100 個の周波数のうち、最も低い 10 個の周波数のみを使用して `y` を生成し、その他の特徴量は情報を提供しません。これにより、ある程度の L1 ペナルティが必要な高次元疎な特徴空間が生成されます。

```python
import numpy as np

rng = np.random.RandomState(0)
n_samples, n_features, n_informative = 50, 100, 10
time_step = np.linspace(-2, 2, n_samples)
freqs = 2 * np.pi * np.sort(rng.rand(n_features)) / 0.01
X = np.zeros((n_samples, n_features))

for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step)

idx = np.arange(n_features)
true_coef = (-1) ** idx * np.exp(-idx / 10)
true_coef[n_informative:] = 0  # sparsify coef
y = np.dot(X, true_coef)

# introduce random phase using numpy.random.random_sample
# add some gaussian noise using numpy.random.normal
for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step + 2 * (rng.random_sample() - 0.5))
    X[:, i] += 0.2 * rng.normal(0, 1, n_samples)

y += 0.2 * rng.normal(0, 1, n_samples)

# split the data into train and test sets using train_test_split from sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=False)
```
