# 異なるアルファ値を持つ棒グラフの作成

このステップでは、Matplotlib の `bar` メソッドを使用して棒グラフを作成します。`(matplotlib_color, alpha)` という色の書式を使用してアルファ値を設定します。グラフ内の各棒は、その y 値に基づいて異なるアルファ値を持ちます。

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility.
np.random.seed(19680801)

fig, ax = plt.subplots()

x_values = [n for n in range(20)]
y_values = np.random.randn(20)

facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors

# Normalize y values to get distinct face alpha values.
abs_y = [abs(y) for y in y_values]
face_alphas = [n / max(abs_y) for n in abs_y]
edge_alphas = [1 - alpha for alpha in face_alphas]

colors_with_alphas = list(zip(facecolors, face_alphas))
edgecolors_with_alphas = list(zip(edgecolors, edge_alphas))

ax.bar(x_values, y_values, color=colors_with_alphas,
        edgecolor=edgecolors_with_alphas)
ax.set_title('Normalized alphas for\neach bar and each edge')

plt.show()
```
