# データの生成

まず、モデルに適合させるためのサンプルデータを生成する必要があります。numpy を使って 100 個のサンプルを生成し、それぞれ 30 個の特徴と 40 個のタスクを持たせます。また、5 つの関連する特徴をランダムに選択し、ランダムな周波数と位相の正弦波を使ってそれらに係数を作成します。最後に、データにいくつかのランダムノイズを追加します。

```python
import numpy as np

rng = np.random.RandomState(42)

# ランダムな周波数と位相の正弦波を使った 2 次元係数を生成する
n_samples, n_features, n_tasks = 100, 30, 40
n_relevant_features = 5
coef = np.zeros((n_tasks, n_features))
times = np.linspace(0, 2 * np.pi, n_tasks)
for k in range(n_relevant_features):
    coef[:, k] = np.sin((1.0 + rng.randn(1)) * times + 3 * rng.randn(1))

X = rng.randn(n_samples, n_features)
Y = np.dot(X, coef.T) + rng.randn(n_samples, n_tasks)
```
