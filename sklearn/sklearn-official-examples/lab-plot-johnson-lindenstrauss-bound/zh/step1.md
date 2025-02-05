# 理论界限

第一步是探索约翰逊 - 林登施特劳斯引理的理论界限。我们将绘制为保证对不断增加的样本数量 `n_samples` 进行 `eps` 嵌入所需的最小维度数。随机投影 `p` 引入的失真由以下事实确定：`p` 以良好的概率定义了一个 `eps` 嵌入，定义如下：

`(1 - eps) \|u - v\|^2 < \|p(u) - p(v)\|^2 < (1 + eps) \|u - v\|^2`

其中 `u` 和 `v` 是从形状为 `(n_samples, n_features)` 的数据集中选取的任意行，并且 `p` 是由形状为 `(n_components, n_features)` 的随机高斯 `N(0, 1)` 矩阵（或稀疏阿赫利奥普塔斯矩阵）进行的投影。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.random_projection import johnson_lindenstrauss_min_dim

# 可接受失真范围
eps_range = np.linspace(0.1, 0.99, 5)
colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(eps_range)))

# 要嵌入的样本数量（观测值）范围
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
