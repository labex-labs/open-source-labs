# データセットの生成

単一の特徴量`x`との线形関系を使って、同じ期待値を持つ2つの合成データセットを生成します。データセットには、异方分散性のノルマルノイズと非対称パレートノイズを追加します。

```python
import numpy as np

rng = np.random.RandomState(42)
x = np.linspace(start=0, stop=10, num=100)
X = x[:, np.newaxis]
y_true_mean = 10 + 0.5 * x

# 异方分散性のノルマルノイズ
y_normal = y_true_mean + rng.normal(loc=0, scale=0.5 + 0.5 * x, size=x.shape[0])

# 非対称パレートノイズ
a = 5
y_pareto = y_true_mean + 10 * (rng.pareto(a, size=x.shape[0]) - 1 / (a - 1))
```
