# 理論的な境界

最初のステップは、ヨンソン・リンデンシュトラウスの補題の理論的な境界を調べることです。サンプル数 `n_samples` が増えるにつれて、`eps` 埋め込みを保証するために必要な最小次元数をプロットします。ランダム射影 `p` によって導入される歪みは、`p` が以下の定義による良好な確率で `eps` 埋め込みを定義しているという事実によって主張されます。

`(1 - eps) \|u - v\|^2 < \|p(u) - p(v)\|^2 < (1 + eps) \|u - v\|^2`

ここで、`u` と `v` は形状 `(n_samples, n_features)` のデータセットから取られる任意の行であり、`p` は形状 `(n_components, n_features)` のランダムなガウス `N(0, 1)` 行列（または疎なアクリオプタス行列）による射影です。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.random_projection import johnson_lindenstrauss_min_dim

# range of admissible distortions
eps_range = np.linspace(0.1, 0.99, 5)
colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(eps_range)))

# range of number of samples (observation) to embed
n_samples_range = np.logspace(1, 9, 9)

plt.figure()
for eps, color in zip(eps_range, colors):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples_range, eps=eps)
    plt.loglog(n_samples_range, min_n_components, color=color)

plt.legend([f"eps = {eps:0.1f}" for eps in eps_range], loc="lower right")
plt.xlabel("Number of observations to eps-embed")
plt.ylabel("Minimum number of dimensions")
plt.title("Johnson-Lindenstrauss bounds:\nn_samples vs n_components")
plt.show()
```
